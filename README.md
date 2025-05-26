# Pendências Contábeis

## Descrição

Este sistema é uma aplicação desktop desenvolvida em Python com PySide6 (Qt) para gerenciamento de pendências contábeis de empresas. O objetivo é facilitar o controle, envio e histórico de pendências e impostos, além de automatizar o envio de emails para os responsáveis de cada empresa.

## Funcionalidades

- Cadastro, edição e remoção de empresas.
- Cadastro, edição e remoção de impostos.
- Cadastro e gerenciamento de pendências contábeis por empresa.
- Cadastro e gerenciamento de emails para cada empresa.
- Envio automatizado de emails com as pendências e impostos para os endereços cadastrados.
- Geração de relatórios de envio em formato de planilha.
- Histórico de envios realizados.
- Interface gráfica intuitiva e responsiva.
- Integração com banco de dados MySQL (requer Docker para o banco).

## Estrutura do Projeto

- `src/main.py`: Arquivo principal da aplicação, contendo a lógica da interface gráfica e integração com os módulos.
- `database.py`: Módulo de acesso ao banco de dados.
- `pendency.py`: Módulo para gerenciamento das pendências.
- `address.py`: Módulo para gerenciamento dos emails das empresas.
- `postman.py`: Módulo responsável pelo envio de emails.
- `sheet.py`: Módulo para geração de relatórios em planilha.
- `local_changes.py`: Gerencia alterações locais e preferências do usuário.
- `window_pend.py`: Interface gráfica gerada pelo Qt Designer.
- `imgs/`: Pasta com ícones e imagens utilizadas na interface.

## Requisitos

- Python 3.8+
- PySide6
- pymysql
- python-dateutil
- Docker (para o banco de dados MySQL)
- Outros módulos listados em `requirements.txt`

## Como Executar

1. Certifique-se de que o Docker está instalado e em execução.
2. Suba o container do banco de dados MySQL conforme instruções do projeto.
3. Instale as dependências Python:
   ```
   pip install -r requirements.txt
   ```
4. Execute o programa:
   ```
   python src/main.py
   ```

## Observações

- O sistema utiliza um banco de dados MySQL hospedado via Docker. Certifique-se de que o container está ativo antes de iniciar a aplicação.
- O envio de emails requer configuração prévia de servidor SMTP (verifique o módulo `postman.py`).
- O layout da interface pode ser customizado via Qt Designer e recompilado para Python.

## Licença

Este projeto é de uso interno e não possui licença aberta.

