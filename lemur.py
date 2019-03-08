from PIL import Image

def main():
    pathname = './data/2015.208039.Alices-Adventures_0000.bmp'
    im = Image.open(pathname)
    pixels = [] #RGB pixels for the new image
    for y in range(0,im.height):
        print(im.height-y)
        for x in range(0,im.width):
            position = x,y
            pixelvalue = im.getpixel(position)
            if pixelvalue==255:
                RGB_values = [6,34,200]
            else:
                RGB_values = [pixelvalue, pixelvalue, pixelvalue]
            pixels.extend(RGB_values)
    im2 = Image.frombytes('RGB', im.size, bytes(pixels))
    im2.show()

if __name__ == '__main__':
    main()