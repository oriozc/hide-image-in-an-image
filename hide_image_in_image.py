import PIL.Image
import io


img = PIL.Image.open('second_image.png')
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')


with open('main_image.jpg', 'ab') as f:
    f.write(byte_arr.getvalue())