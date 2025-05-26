from pathlib import Path

class LocalChanges:
    """
    Gerencia alterações e preferências locais do usuário, como o nome do remetente.
    """
    def __init__(self):
        self.path = Path(__file__).parent / 'txt' / 'log_use.txt'
        pass

    def sender_name(self):
        """
        Lê o nome do remetente salvo localmente.
        Returns:
            str: Nome do remetente.
        """
        with open(self.path, 'r') as file:
            return file.read()

    def updt_sender(self, name: str):
        """
        Atualiza o nome do remetente, caso tenha sido alterado.
        Args:
            name (str): Novo nome do remetente.
        """
        current_name = self.sender_name()
        if name != current_name:
            with open(self.path, 'w') as file:
                file.write(name)
