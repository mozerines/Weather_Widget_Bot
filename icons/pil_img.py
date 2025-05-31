from PIL import Image
import io


def img_generation(maket, icon: str) -> Image:
    maket = Image.open(maket)
    icon = Image.open(icon)
    test1 = maket.crop(box=(0, 426, 640, 1100))


    test = maket.crop(box=(793, 759, 793, 759))
    test1.save(fp='test1.png', format='PNG')


    pass

def img_to_media(image: str) -> io.BytesIO:
    img = Image.open(image)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr


print(img_to_media('11d@2x.png'))

img_generation(maket='sun_maket.jpg', icon='10d@2x.png')

