from pymysql import err, connect
from dotenv import load_dotenv
from pathlib import Path
from os import getenv
from pedency_table import PedencyTable

load_dotenv(Path(__file__).parent / 'env' / '.env')

class DataBase:
    COMPANIES_TABLE = 'Companies'
    PENDING_TABLE = 'Pending'
    TABELA_USUARIO = 'Usuario'
    TABELA_EMAIL = 'Email'

    def __init__(self) -> None:
        self.connection = connect(
                host= getenv('IP_HOST'),
                port= int(getenv('PORT_HOST')),
                user= getenv('USER'),
                password= getenv('PASSWORD'),
                database= getenv('DB'),
            )
        
        self.columns_pending = ['id_pending', 'type', 'value', 'competence', 'maturity', 'observations']

        self.query_endereco = (
            f'SELECT endereco FROM {self.TABELA_EMAIL} '
            'WHERE id_emp IN '
            f'(SELECT id_emp FROM {self.COMPANIES_TABLE} '
            'WHERE nome = %s)'
        )

        self.update_endereco = (
            f'UPDATE {self.TABELA_EMAIL} SET '
            'endereco = %s '
            'WHERE endereco = %s AND  id_emp = %s'
        )

        self.insert_endereco = (
            f'INSERT INTO {self.TABELA_EMAIL} '
            '(endereco, id_emp)'
            ' VALUES (%s, %s) '
        )

        self.delete_endereco = (
            f'DELETE FROM {self.TABELA_EMAIL} '
            'WHERE id_emp = %s AND endereco = %s'
        )

        self.delete_enderecos = (
            f'DELETE FROM {self.TABELA_EMAIL} '
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

        self.insert_empresa = (
            f'INSERT INTO {self.COMPANIES_TABLE} '
            '(nome) VALUES (%s) '
        )

        self.delete_empresa = (
            f'DELETE FROM {self.COMPANIES_TABLE} '
            'WHERE id_emp = %s'
        )
        
        self.query_ass = (
            f'SELECT assinatura FROM {self.TABELA_USUARIO} '
            'WHERE nome = %s'
        )

        self.query_acessorias = (
            'SELECT email_acessorias, senha_acessorias'
            f' FROM {self.TABELA_USUARIO} '
            'WHERE nome = %s'
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
            #dict[str,list]]
            data = {key: [] for key in self.columns_pending}
            for sub in cursor.fetchall():
                for index, i in enumerate(sub):
                    data[self.columns_pending[index]].append(i)
            
            return PedencyTable(self.columns_pending, data)

    def user_acessorias(self, nome_func: str):
        with self.connection.cursor() as cursor:
            cursor.execute(
                self.query_acessorias, (nome_func,)
            )
            return cursor.fetchone()