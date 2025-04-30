from pymysql import err, connect
from dotenv import load_dotenv
from pendency import Pedency
from address import Address
from pathlib import Path
from os import getenv
from change import Change
from datetime import date
from copy import deepcopy

load_dotenv(Path(__file__).parent / 'env' / '.env')

class DataBase:
    COMPANIES_TABLE = 'Companies'
    PENDING_TABLE = 'Pending'
    EMAIL_TABLE = 'Emails'

    def __init__(self) -> None:
        self.connection = connect(
                host= getenv('IP_HOST'),
                port= int(getenv('PORT_HOST')),
                user= getenv('USER'),
                password= getenv('PASSWORD'),
                database= getenv('DB'),
            )
        
        self.columns_pending = ['id_pending', 'type', 'value', 'competence', 'maturity', 'observations']

        self.ref_key_pedency = {
                'Valor': lambda value: float(value.replace(',','.')),
                'Competência': self.__tranform_competence,
                'Vencimento': self.__transform_maturity,
        }

        self.query_endereco = (
            f'SELECT endereco FROM {self.EMAIL_TABLE} '
            'WHERE id_emp IN '
            f'(SELECT id_emp FROM {self.COMPANIES_TABLE} '
            'WHERE nome = %s)'
        )

        self.update_endereco = (
            f'UPDATE {self.EMAIL_TABLE} SET '
            'endereco = %s '
            'WHERE endereco = %s AND  id_emp = %s'
        )

        self.insert_endereco = (
            f'INSERT INTO {self.EMAIL_TABLE} '
            '(endereco, id_emp)'
            ' VALUES (%s, %s) '
        )

        self.delete_endereco = (
            f'DELETE FROM {self.EMAIL_TABLE} '
            'WHERE id_emp = %s AND endereco = %s'
        )

        self.delete_enderecos = (
            f'DELETE FROM {self.EMAIL_TABLE} '
            'WHERE id_emp = %s'
        )

        self.query_companies = (
            f'SELECT id_companies, name FROM {self.COMPANIES_TABLE} '
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

        self.insert_empresa = (
            f'INSERT INTO {self.COMPANIES_TABLE} '
            '(nome) VALUES (%s) '
        )

        self.delete_empresa = (
            f'DELETE FROM {self.COMPANIES_TABLE} '
            'WHERE id_emp = %s'
        )

        self.insert_pedency = (
            f'INSERT INTO {self.PENDING_TABLE} '
            '(value, competence, maturity, type, observations)'
            ' VALUES (%s, %s, %s, %s, %s) '
        )

        self.insert_email = (
            f'INSERT INTO {self.EMAIL_TABLE} '
            '(address, id_companies) VALUES (%s, %s)'
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

    def emails_empresa(self, nome_empresa: str) -> list[str]:
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.query_endereco, (nome_empresa,)
            )
            return [i for sub in cursor.fetchall() for i in sub]
    
    def remover_empresa(self, id_empresa: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.delete_empresa, (id_empresa, )
            )
            self.connection.commit()

    def remover_endereco(self, id_empresa: str, endereco: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.delete_endereco, (id_empresa, endereco)
            )
            self.connection.commit()

    def remover_enderecos(self, id_empresa: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.delete_enderecos, (id_empresa,)
            )
            self.connection.commit()
    
    def atualizar_endereco(self, end_novo: str, end_antigo: str, id_emp: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.update_endereco, (end_novo, end_antigo, id_emp)
            )
            self.connection.commit()

    def registrar_empresa(self, nome_empresa: str) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.insert_empresa, (nome_empresa,)
            )
            self.connection.commit()
    
    def companies(self) -> list[str]:
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.query_companies
            )
            return {sub[0] : sub[1]  for sub in cursor.fetchall()}

    def registrar_enderecos(self, enderecos: list[str], id_empresa: str) -> None:
        with self.connection.cursor() as cursor:
            cursor.executemany(
                self.insert_endereco, 
                ([endereco, id_empresa] for endereco in enderecos)
            )
            self.connection.commit()

    def pedency(self, companie_id: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.query_pedency, (companie_id,)
            )
            data = {key: [] for key in self.columns_pending}
            for sub in cursor.fetchall():
                for index, i in enumerate(sub):
                    data[self.columns_pending[index]].append(i)
            
            ids = data.pop('id_pending')
            return Pedency(ids, data)

    def emails(self, companie_id: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.query_emails, (companie_id,)
            )

            id = []
            address = []
            for sub in cursor.fetchall():
                id.append(sub[0])
                address.append(sub[1])
            
            return Address(id, address)
        
    def changes_pedency(self, id_companie: str, change: Change):
        #add:list, updt: dict[tuple[dict]], remove: list[int]
        add, updt, remove = change.data()
        
        #ADD


        #UPDATE
        # with self.connection.cursor() as cursor:
        #     infos = self.__transform_pedency(id_companie, updt)
        #     cursor.executemany(
        #         self.update_pedency,
        #         infos
        #     )
        #     self.connection.commit()
        
        #REMOVE
        # self.__remove_change(id_companie, self.delete_pedency, remove)

    def __transform_pedency(self, id_companie, updt):
        infos = ()
        for id_data, data in updt.items():
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
        with self.connection.cursor() as cursor:
            cursor.executemany(
                self.insert_email, 
                ([address, id_companie] for address in add)
            )
            self.connection.commit()

        #UPDATE - Falta azul no Main
        with self.connection.cursor() as cursor:
            cursor.executemany(
                self.update_emails, 
                ([adderss, id_companie, id_address] \
                    for id_address, adderss in updt.items())
            )
            self.connection.commit()

        #REMOVE
        self.__remove_change(id_companie, self.delete_email, remove)

    def __remove_change(self, id_companie: str, query: str, data: list[str]):
        with self.connection.cursor() as cursor:
            cursor.executemany(
                query, 
                ([id_companie, id_data] for id_data in data)
            )
            self.connection.commit()