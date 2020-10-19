from PIL import Image

img = Image.open('baby.jpeg')
# img.show()
rotate_img = img.transpose(Image.FLIP_LEFT_RIGHT)


rotate_img.show()
