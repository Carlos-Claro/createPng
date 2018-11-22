import os
from PIL import Image
from resizeimage import resizeimage

# https://github.com/charlesthk/python-resize-image
class myPNG(object):

    def __init__(self):
        self.executa()



    def executa(self):
        for image in os.listdir('images'):
            nome = image[3:-4]
            for tamanho in self.tamanhos():
                self.geraImages(image,nome,tamanho)
                # print(nome)
                # print(image)
                # print(tamanho)


    def geraImages(self,image,nome,tamanho):
        with open('images/'+image, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_thumbnail(image, [tamanho, tamanho])
                cover.save('images_modificadas/' + nome + '-' + str(tamanho) + 'x' + str(tamanho)+'.png', 'png')


    def tamanhos(self):
        tamanho = [48,96,128,144,152,192,512]
        return tamanho


if __name__ == '__main__':
    try:
        myPNG()
        #c.getItens()
    except KeyboardInterrupt:
        pass
    finally:
        print("Finaliza myPNG")
