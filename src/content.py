from pathlib import Path
import datetime
import pandas as pd

class Content:
    def __init__(self):
        self.CONTENT_BASE = Path(__file__).parent / 'src' / 'html' / 'content_email.html'
        with open (self.CONTENT_BASE, 'r', encoding='utf-8') as file:
            self.body = file.read()

    # def add_linha(self, row):
    #     valor_pag = float(row['Valor'].replace('.','').replace(',', '.'))

    #     dia_atual = datetime.now()
    #     dia_vencimento = datetime.strptime(row['Vencimento'], '%d/%m/%Y')
    #     dias_atraso = (dia_atual - dia_vencimento).days

    #     multa = round(valor_pag * self.VALOR_JUROS , 2)

    #     juros = round(((valor_pag * self.VALOR_JUROS) / 30) * dias_atraso , 2)
        
    #     total = round(valor_pag + multa + juros , 2)

    #     self.valores_totais.append(total)

    #     self.text = self.text + """
    #         <tr>
    #             <th style="border: 1px solid black; padding: 8px 10px;">{0}</th>
    #             <td style="border: 1px solid black; padding: 8px 10px;">{1}</td>
    #             <td style="text-align: center; border: 1px solid black; padding: 8px 10px;">{2}</td>
    #             <td style="color: red; border: 1px solid black; padding: 8px 10px;">R$ {3}</td>
    #             <td style="border: 1px solid black; padding: 8px 10px;">R$ {4}</td>
    #             <td style="border: 1px solid black; padding: 8px 10px;">R$ {5}</td>
    #             <td style="border: 1px solid black; padding: 8px 10px;"><span style="color: red;">R$ {6}</span></td>\
    #         </tr>\n
    #         """.format(
    #                 str(row['Competência']), 
    #                 str(row['Vencimento']), 
    #                 dias_atraso, str(row['Valor']), 
    #                 f'{multa:_.2f}'.replace('.',',').replace('_','.'), 
    #                 f'{juros:_.2f}'.replace('.',',').replace('_','.'), 
    #                 f'{total:_.2f}'.replace('.',',').replace('_','.')
    #             )

    def create(self, dataFrame: pd.DataFrame) -> str:
        return self.body.replace('$table', dataFrame.to_html())\
                    .replace('$greeting', self.cumprimento())

    def cumprimento(self):
        hora_atual = datetime.now().hour
        if hora_atual < 12:
            return 'bom dia!'
        elif hora_atual >= 12 and hora_atual < 18:
            return 'boa tarde!'
        return 'boa noite!'