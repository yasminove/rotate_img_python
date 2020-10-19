# from PIL import Image
#
# img = Image.open('baby.jpeg')
# img.show()
# # rotate_img = img.transpose(Image.)


from PIL import Image

img = Image.open('baby.jpeg')

flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)

spin_img = img.transpose(Image.ROTATE_90)

# img.show()
spin_img.show()