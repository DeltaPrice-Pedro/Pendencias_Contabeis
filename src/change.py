class Change:
    """
    Classe utilitária para armazenar alterações (adicionar, atualizar, remover) em listas de dados.
    """
    def __init__(self):
        self.add = []
        self.updt = {}
        self.remove = []
        pass

    def to_add(self, *args):
        """
        Adiciona um item à lista de adições.
        """
        self.add.append(*args)

    def to_updt(self, id, *args):
        """
        Adiciona/atualiza um item à lista de atualizações.
        """
        self.updt[id] = args
    
    def to_remove(self, id):
        """
        Adiciona um item à lista de remoções.
        """
        self.remove.append(id)

    def data(self):
        """
        Retorna as listas de adições, atualizações e remoções.
        Returns:
            tuple: (add, updt, remove)
        """
        return self.add, self.updt, self.remove
