from smtp2go.core import Smtp2goClient
from pathlib import Path
from os import  getenv
import base64

class DeltaMail:
    def __init__(self, companie: str, address: list[str], content: str):
        self.client = Smtp2goClient(api_key= getenv('API_SMTP'))
        self.sender = getenv('SENDER_EMAIL')

        # address.append(self.sender)
        self.payload = {
            'sender': self.sender,
            'recipients': address,
            'subject': f'{companie} - PENDÊNCIAS CONTÁBEIS',
            'html': content,
        }

    def attach(self, assign_filename: Path):
        with open(assign_filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        self.payload['inlines'] = [
            {
                'filename': assign_filename.name.__str__(),
                'fileblob': encoded_string,
                'mimetype': 'image/png'
            }
        ]

    def send(self):
        # ...
        response = self.client.send(**self.payload)
        if response.success == False:
            raise Exception('Endereço de email inválido')