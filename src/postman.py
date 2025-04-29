from PySide6.QtCore import QObject, Signal
# from PySide6.QtWidgets import
import pandas as pd
from content import Content
from delta_mail import DeltaMail

class Postman(QObject):

    result = Signal(str)
    end = Signal()

    def __init__(self, companie: str, address: list[str], pedency: dict[list]):
        super().__init__()
        self.companie = companie
        self.address = address
        self.pedency = pedency
        self.result_message = f'Pendências da empresa - {companie} - forem enviadas com sucesso para os endereços:\n|=>{'\n|=>'.join(self.address)}'
        pass

    def execute(self):
        try:
            df = pd.DataFrame(self.pedency)

            content = Content()
            html = content.create(df)

            delta_mail = DeltaMail(self.companie, self.address, html)
            delta_mail.send()
            
            self.result.emit(self.result_message)
        except Exception as error:
            self.result.emit(error)

        # conteudo_atual.add_linha(pd.Series(data= {
        #     'Competência': competencia,
        #     'Vencimento': vencimento,
        #     'Valor': row.Valor
        # }))