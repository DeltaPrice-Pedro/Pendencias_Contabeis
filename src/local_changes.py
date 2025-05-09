from pathlib import Path

class LocalChanges:
    def __init__(self):
        self.path = Path(__file__).parent / 'txt' / 'log_use.txt'
        pass

    def sender_name(self):
        with open(self.path, 'r') as file:
            return file.read()

    def updt_sender(self, name: str):
        current_name = self.sender_name()
        if name != current_name:
            with open(self.path, 'w') as file:
                file.write(name)
