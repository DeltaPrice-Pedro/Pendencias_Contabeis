import spire.doc as sd
from PIL import Image

class ImageEditor:
    def __init__(self) -> None:
        self.AREA_CORTE = (0, 50, 1524, 564)
        #(esquerda, topo, direita, baixo)
        pass

    def png_image(self, png_path : str, docx_path : str):
        document = sd.Document(docx_path)
        imageStream = document.SaveImageToStreams(0, sd.ImageType.Bitmap)
        
        with open(png_path,'wb') as imageFile:
            imageFile.write(imageStream.ToArray())
        document.Close()

        self.__crop(png_path)

    def __crop(self, png_path):
        image = Image.open(png_path)
        croped_image = image.crop(self.AREA_CORTE)
        croped_image.save(png_path)
