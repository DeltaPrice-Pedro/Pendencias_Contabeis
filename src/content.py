from pathlib import Path
from datetime import datetime
import pandas as pd

class Content:
    def __init__(self):
        self.CONTENT_BASE = Path(__file__).parent / 'html' / 'content_email.html'
        with open (self.CONTENT_BASE, 'r', encoding='utf-8') as file:
            self.body = file.read()

    def create(self, df_pedency: pd.DataFrame, df_taxes: pd.DataFrame) -> str:
        return self.body\
                .replace('$table_pedency', df_pedency.to_html())\
                    .replace('$table_taxes', df_taxes.to_html())\
                        .replace('$greeting', self.cumprimento())

    def cumprimento(self):
        hora_atual = datetime.now().hour
        if hora_atual < 12:
            return 'bom dia!'
        elif hora_atual >= 12 and hora_atual < 18:
            return 'boa tarde!'
        return 'boa noite!'