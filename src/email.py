from smtp2go.core import Smtp2goClient
from os import  getenv

class Email:
    def __init__(self):
        self.client = Smtp2goClient(api_key= getenv('API_SMTP'))
        self.base_titulo = ' - HONORÁRIOS CONTÁBEIS EM ABERTO'
        self.sender = getenv('SENDER_EMAIL')

    def create(self, destinatarios: list[str], nome_empresa: str, conteudo: str):
        destinatarios.append(self.sender)
        self.payload = {
            'sender': self.sender,
            'recipients': destinatarios,
            'subject': nome_empresa  + self.base_titulo,
            'html': conteudo,
        }

    def send(self):
        ...
        # response = self.client.send(**self.payload)
        # if response.success == False:
            # raise Exception('Endereço de email inválido')