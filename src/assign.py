import os
from pathlib import Path
from image_editor import ImageEditor
from docxtpl import DocxTemplate

class Assign:
    """
    Gera a assinatura personalizada do usuário em formato de imagem a partir de um template DOCX.
    """
    def __init__(self, name_func: str):
        self.name_func = name_func

        self.base_ass = Path(__file__).parent / 'docx' / 'base_assinaturas_25y.docx'

        self.DOCX_FILE_NAME = Path(__file__).parent / 'assign_word.docx'
        self.PNG_FILE_NAME = Path(__file__).parent / 'assign.png'

        self.KEY_NOME = 'nome'
        self.KEY_IMG = 'img'
        pass

    def __call__(self, *args, **kwds):
        """
        Gera a assinatura em PNG a partir do template DOCX.
        Returns:
            Path: Caminho do arquivo PNG gerado.
        """
        ref = {self.KEY_NOME: self.name_func}
        self.__render(ref)
        ImageEditor().png_image(
            self.PNG_FILE_NAME.__str__(), self.DOCX_FILE_NAME.__str__()
        )
        os.remove(self.DOCX_FILE_NAME)

        return self.PNG_FILE_NAME
    
    def __render(self, ref):
        """
        Renderiza o template DOCX com os dados fornecidos.
        """
        self.caminho = DocxTemplate(self.base_ass)
        self.caminho.render(ref)
        self.caminho.save(self.DOCX_FILE_NAME)

    def remove_image(self):
        """
        Remove a imagem de assinatura gerada.
        """
        os.remove(self.PNG_FILE_NAME)

