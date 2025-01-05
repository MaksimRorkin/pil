from PIL import Image, ImageFilter

with Image.open("pig.jpg") as photo:
    print(photo.size)
    print(photo.format)
    print(photo.mode)

    photo = photo.convert('1')
    photo = photo.filter(ImageFilter.BLUR)
    photo = photo.transpose(Image.ROTATE_90)

    photo.save("new_photo.jpg")
   

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Фай не знайдено!')
        self.original.show()

    def black_white(self):
        bw_photo = self.original.convert('L')
        self.changed.append(bw_photo)
        bw_photo.show()

    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        rotated.show()

    def do_cropped(self):
        box = (250, 100, 600, 400)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        cropped.show() 

MyImage = ImageEditor('pig.jpg')
MyImage.open()
MyImage.black_white()
MyImage.do_left()
MyImage.do_cropped()







#photo.show()