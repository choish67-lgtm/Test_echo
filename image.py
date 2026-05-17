from PIL import Image
from PIL import ImageFilter

def main():
    img = Image.open("jinwoo.jpg")
    img.close()
    with Image.open("jinwoo.jpg") as img:
        print(img.size)
        print(img.format)
        img = img.rotate(360)
        #img = img.filter(ImageFilter.BLUR)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("jinwoo_out3.jpg")

main()

