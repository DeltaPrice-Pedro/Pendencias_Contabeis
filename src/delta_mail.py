from smtp2go.core import Smtp2goClient
from os import  getenv

class DeltaMail:
    def __init__(self, companie: str, address: list[str], content: str):
        self.client = Smtp2goClient(api_key= getenv('API_SMTP'))
        self.sender = getenv('SENDER_EMAIL')

        address.append(self.sender)
        self.payload = {
            'sender': self.sender,
            'recipients': address,
            'subject': f'{companie} - PENDÊNCIAS CONTÁBEIS',
            'html': content,
        }

    def send(self):
        # ...
        response = self.client.send(**self.payload)
        if response.success == False:
            raise Exception('Endereço de email inválido')