from pathlib import Path
from datetime import datetime
import pandas as pd

class Content:
    def __init__(self):
        self.CONTENT_BASE = Path(__file__).parent / 'html' / 'content_email.html'
        self.red_color_formatter = {
            'Valor': lambda x: f'<span style="color: red;"> R$ {x} </span>'
        }

    def html(self, df_pedency: pd.DataFrame, df_taxes: pd.DataFrame) -> str:
        ref = {
            120: df_pedency,
            80: df_taxes
        }
        
        with open (self.CONTENT_BASE, 'r', encoding='utf-8') as file:
            body = file.read()

        html_tables = []
        for col_space, df in ref.items():
            html_tables.append(
                df.to_html(
                    col_space= col_space, index= False, justify='center',
                    formatters= self.red_color_formatter
                ).replace('&lt;', '<').replace('&gt;', '>')
            )

        return body.format(
                    table_pedency = html_tables[0],
                    table_taxes = html_tables[1],
                    greeting = self.greeting(),
                    img = self.image_path,
                    subtype = 'html',
                    alt = self.alt,
                )
    
    def attach(self, image_path, name_func):
        self.image_path = image_path
        self.alt = name_func,
        
    def greeting(self):
        hora_atual = datetime.now().hour
        if hora_atual < 12:
            return 'bom dia!'
        elif hora_atual >= 12 and hora_atual < 18:
            return 'boa tarde!'
        return 'boa noite!'