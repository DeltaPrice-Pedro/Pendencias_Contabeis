from PySide6.QtCore import QObject, Signal
# from PySide6.QtWidgets import
import pandas as pd
from content import Content
from delta_mail import DeltaMail
from assign import Assign

class Postman(QObject):
    sended = Signal(str, str, list)
    result = Signal(str)
    end = Signal()

    def __init__(self, name_func: str, companie: str, address: list[str], pedency: dict[list], taxes: dict[list]):
        super().__init__()
        self.name_func = name_func
        self.companie = companie
        self.address = address
        self.pedency = pedency
        self.taxes = taxes
        self.result_message = f'Pendências da empresa - {companie} - forem enviadas com sucesso para o(s) endereço(s):\n|=>{'\n|=>'.join(self.address)}'
        pass

    def execute(self):
        try:
            df_pedency = pd.DataFrame(self.pedency)
            df_taxes = pd.DataFrame(self.taxes)

            content = Content()
            assign = Assign(self.name_func)
            assign_filename = assign()

            content.attach(assign_filename.name.__str__())
            html = content.html(df_pedency, df_taxes)

            delta_mail = DeltaMail(self.companie, self.address, html)
            delta_mail.attach(assign_filename)

            delta_mail.send()
            
            assign.remove_image()
            
            self.sended.emit(
                self.name_func, self.companie, list(self.taxes.values())
            )
            self.result.emit(self.result_message)
            self.end.emit()
        except Exception as error:
            self.result.emit(error)

        # conteudo_atual.add_linha(pd.Series(data= {
        #     'Competência': competencia,
        #     'Vencimento': vencimento,
        #     'Valor': row.Valor
        # }))