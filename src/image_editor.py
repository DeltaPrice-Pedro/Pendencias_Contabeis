import spire.doc as sd
from PIL import Image

class ImageEditor:
    """
    Classe utilitária para manipulação de imagens extraídas de arquivos DOCX.
    Permite converter a primeira página de um DOCX em PNG e realizar corte na imagem.
    """
    def __init__(self) -> None:
        # Área de corte: (esquerda, topo, direita, baixo)
        self.AREA_CORTE = (0, 50, 1524, 564)
        pass

    def png_image(self, png_path : str, docx_path : str):
        """
        Extrai a primeira página do arquivo DOCX como imagem PNG e realiza o corte.
        Args:
            png_path (str): Caminho para salvar a imagem PNG.
            docx_path (str): Caminho do arquivo DOCX de origem.
        """
        document = sd.Document(docx_path)
        imageStream = document.SaveImageToStreams(0, sd.ImageType.Bitmap)
        
        with open(png_path,'wb') as imageFile:
            imageFile.write(imageStream.ToArray())
        document.Close()

        self.__crop(png_path)

    def __crop(self, png_path):
        """
        Realiza o corte da imagem PNG conforme a área definida.
        Args:
            png_path (str): Caminho da imagem PNG a ser cortada.
        """
        image = Image.open(png_path)
        croped_image = image.crop(self.AREA_CORTE)
        croped_image.save(png_path)
