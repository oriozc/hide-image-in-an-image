import io

import PIL.Image

with open('main_image.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))
    f.seek(offset + 2)

    secret_img = PIL.Image.open(io.BytesIO(f.read()))
    secret_img.save("secret_image.png")