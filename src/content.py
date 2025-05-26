from pathlib import Path
from datetime import datetime
import pandas as pd

class Content:
    """
    Responsável por gerar o conteúdo HTML dos emails enviados pelo sistema.
    """
    def __init__(self):
        self.CONTENT_BASE = Path(__file__).parent / 'html' / 'content_email.html'
        self.red_color_formatter = {
            'Valor': lambda x: f'<span style="color: red;"> R$ {x} </span>'
        }

    def html(self, 
            df_pedency: pd.DataFrame, 
            df_taxes: pd.DataFrame,
            assign: Path, 
            name_func: str
            ) -> str:
        """
        Gera o HTML do email a partir dos dados de pendências, impostos e assinatura.
        """
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
                    img = assign.stem,
                    alt = name_func
                )
    
    def greeting(self):
        """
        Retorna uma saudação apropriada de acordo com o horário atual.
        """
        hora_atual = datetime.now().hour
        if hora_atual < 12:
            return 'bom dia!'
        elif hora_atual >= 12 and hora_atual < 18:
            return 'boa tarde!'
        return 'boa noite!'