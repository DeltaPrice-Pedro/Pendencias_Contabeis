from pymysql import err, connect
from dotenv import load_dotenv
from pathlib import Path
from os import getenv
from change import Change
from datetime import date, datetime

load_dotenv(Path(__file__).parent / 'env' / '.env')

class DataBase:
    COMPANIES_TABLE = 'Companies'
    PENDING_TABLE = 'Pending'
    EMAIL_TABLE = 'Emails'
    HISTORY_TABLE = 'History'

    def __init__(self) -> None:
        self.connection = connect(
                host= getenv('IP_HOST'),
                port= int(getenv('PORT_HOST')),
                user= getenv('USER'),
                password= getenv('PASSWORD'),
                database= getenv('DB'),
            )
        
        self.columns_pending = ['id_pending', 'type', 'value', 'competence', 'maturity', 'observations']

        self.columns_history = ['Responsável', 'Empresa', 'Data/Hora Envio', 'Registro']

        self.ref_key_pedency = {
                'Valor': lambda value: float(
                    value.replace('.','').replace(',','.')
                ),
                'Competência': self.__tranform_competence,
                'Vencimento': self.__transform_maturity,
        }

        self.query_companies = (
            f'SELECT id_companies, name FROM {self.COMPANIES_TABLE} '
        )

        self.insert_history = (
            f'INSERT INTO {self.HISTORY_TABLE} '
            '(sender, recipient, log_pending, send_datetime, id_companies) '
            'VALUES (%s, %s, %s, %s, %s) '
        )

        self.insert_companie = (
            f'INSERT INTO {self.COMPANIES_TABLE} '
            '(name) VALUES (%s) '
        )

        self.update_companie = (
            f'UPDATE {self.COMPANIES_TABLE} SET '
            'name = %s '
            'WHERE id_companies = %s'
        )

        self.delete_companie = (
            f'DELETE FROM {self.COMPANIES_TABLE} '
            'WHERE id_companies = %s ; '
        )

        self.query_pedency = (
            f'SELECT {', '.join(self.columns_pending) } '
            f'FROM {self.PENDING_TABLE} '
            'WHERE id_companies = %s'
        )

        self.query_emails = (
            'SELECT id_emails, address '
            f'FROM {self.EMAIL_TABLE} '
            'WHERE id_companies = %s'
        )

        self.query_history = (
            'SELECT sender, recipient, send_datetime, log_pending '
            f'FROM {self.HISTORY_TABLE} '
            'WHERE %s <= send_datetime <= %s '
        )

        self.query_history_id = (
            'SELECT sender, recipient, send_datetime, log_pending '
            f'FROM {self.HISTORY_TABLE} '
            'WHERE %s <= send_datetime <= %s '
            'AND id_companies = %s'
        )

        self.insert_email = (
            f'INSERT INTO {self.EMAIL_TABLE} '
            '(address, id_companies) VALUES (%s, %s)'
        )

        self.insert_pedency = (
            f'INSERT INTO {self.PENDING_TABLE} '
            '(value, competence, type, maturity, '
            'observations, id_companies) '
            'VALUES (%(Valor)s, %(Competência)s, '
            '%(Tipo)s, %(Vencimento)s, '
            '%(Observações)s, %(id_companies)s)'
        )

        self.update_pedency = (
            f'UPDATE {self.PENDING_TABLE} SET '
            'value = %(Valor)s, competence = %(Competência)s, '
            'maturity = %(Vencimento)s, type = %(Tipo)s, '
            'observations = %(Observações)s '
            'WHERE id_companies = %(id_companies)s AND '
            'id_pending = %(id_pending)s'
        )

        self.update_emails = (
            f'UPDATE {self.EMAIL_TABLE} SET '
            'address = %s '
            'WHERE id_companies = %s AND id_emails = %s'
        )

        self.delete_pedency = (
            f'DELETE FROM {self.PENDING_TABLE} '
            'WHERE id_companies = %s AND id_pending = %s'
        )

        self.delete_email = (
            f'DELETE FROM {self.EMAIL_TABLE} '
            'WHERE id_companies = %s AND id_emails = %s'
        )
        pass

    def companies(self) -> list[str]:
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.query_companies
            )
            self.connection.commit()

        return {sub[0] : sub[1]  for sub in cursor.fetchall()}
    
    def pedency(self, companie_id: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.query_pedency, (companie_id,)
            )
            self.connection.commit()

        data = {key: [] for key in self.columns_pending}
        for sub in cursor.fetchall():
            for index, i in enumerate(sub):
                data[self.columns_pending[index]].append(i)
            
        ids = data.pop('id_pending')
        return ids, data

    def emails(self, companie_id: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.query_emails, (companie_id,)
            )
            self.connection.commit()

        id = []
        address = []
        for sub in cursor.fetchall():
            id.append(sub[0])
            address.append(sub[1])
        
        return id, address
    
    def history(self, date_from, date_until, id = None):
        if  date_from > date_until:
            raise Exception('Datas inválidas')
        
        query = self.query_history
        data_query = (date_from, date_until)
        
        if id != None:
            query = self.query_history_id
            data_query = data_query + (id,)

        with self.connection.cursor() as cursor:
            cursor.execute(
                query,
                data_query
            )
            self.connection.commit()

        data = {key: [] for key in self.columns_history}
        for sub in cursor.fetchall():
            for index, i in enumerate(sub):
                if self.columns_history[index] == 'Data/Hora Envio':
                    i = i.strftime('%d/%m/%Y, %H:%M:%S')
                data[self.columns_history[index]].append(i)
            
        return data
    
    def add_history(self, name, companie, log, id_companies):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.insert_history, 
                (name, companie, log, datetime.now(), id_companies) 
            )
            self.connection.commit()
        
    def add_companie(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.insert_companie, (name,) 
            )
            self.connection.commit()
        
        return cursor.lastrowid
        
    def edit_companie(self, id, name):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.update_companie, 
                (name, id) 
            )
            self.connection.commit()

    def remove_companie(self, id: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.delete_companie, (id, )
            )
        self.connection.commit()
        
    def changes_pedency(self, id_companie: str, change: Change):
        #add:list, updt: dict[tuple[dict]], remove: list[int]
        add, updt, remove = change.data()
        
        #ADD
        if any(add):
            with self.connection.cursor() as cursor:
                infos = self.__transform_add_pedency(id_companie, add)
                cursor.executemany(
                    self.insert_pedency,
                    infos
                )
                self.connection.commit()

        #UPDATE
        if any(updt):
            with self.connection.cursor() as cursor:
                infos = self.__transform_updt_pedency(id_companie, updt)
                cursor.executemany(
                    self.update_pedency,
                    infos
                )
                self.connection.commit()
        
        #REMOVE
        if any(remove):
            self.__remove_change(id_companie, self.delete_pedency, remove)

    def __transform_add_pedency(self, id_companie: str, add: list[dict]):
        for data in add:
            for key, func in self.ref_key_pedency.items():
                data[key] = func(data[key])
            data['id_companies'] = id_companie
        return add

    def __transform_updt_pedency(self, id_companie, change_values):
        infos = ()
        for id_data, data in change_values.items():
            #Somando tuplas, caso dê errado, enviar dict com keys certas
            data = data[0]
            for key, func in self.ref_key_pedency.items():
                data[key] = func(data[key])

            data['id_pending'] = id_data
            data['id_companies'] = id_companie
            infos = infos + (data,)
        return infos

    def __tranform_competence(self, value):
        comp = [int(value) for value in value.split('/')]
        comp.reverse()
        comp.append(1)
        return date(*comp)
    
    def __transform_maturity(self, value):
        comp = [int(value) for value in value.split('/')]
        comp.reverse()
        return date(*comp)

    def changes_address(self, id_companie: str, change: Change):
        #add: list[str], updt: dict[str], remove: list[int]
        add, updt, remove = change.data()

        #ADD
        if any(add):
            with self.connection.cursor() as cursor:
                cursor.executemany(
                    self.insert_email, 
                    ([address, id_companie] for address in add)
                )
                self.connection.commit()

        #UPDATE - Falta azul no Main
        if any(updt):
            with self.connection.cursor() as cursor:
                cursor.executemany(
                    self.update_emails, 
                    ([adderss, id_companie, id_address] \
                        for id_address, adderss in updt.items())
                )
                self.connection.commit()

        #REMOVE
        if any(remove):
            self.__remove_change(id_companie, self.delete_email, remove)

    def __remove_change(self, id_companie: str, query: str, data: list[str]):
        with self.connection.cursor() as cursor:
            cursor.executemany(
                query, 
                ([id_companie, id_data] for id_data in data)
            )
            self.connection.commit()