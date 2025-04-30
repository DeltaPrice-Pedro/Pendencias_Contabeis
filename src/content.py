from pathlib import Path
from datetime import datetime
import pandas as pd

class Content:
    def __init__(self):
        self.CONTENT_BASE = Path(__file__).parent / 'html' / 'content_email.html'
        with open (self.CONTENT_BASE, 'r', encoding='utf-8') as file:
            self.body = file.read()

    def create(self, df_pedency: pd.DataFrame, df_taxes: pd.DataFrame) -> str:
        html_pedency = df_pedency.to_html(
            col_space= 120, index= False, 
        )

        html_taxes = df_taxes.to_html(
            col_space= 80, index= False,
        )

        return self.body\
                .replace('$table_pedency', html_pedency)\
                        .replace('$table_taxes', html_taxes)\
                                .replace('$greeting', self.greeting())

    def greeting(self):
        hora_atual = datetime.now().hour
        if hora_atual < 12:
            return 'bom dia!'
        elif hora_atual >= 12 and hora_atual < 18:
            return 'boa tarde!'
        return 'boa noite!'