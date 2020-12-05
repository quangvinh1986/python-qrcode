from PIL import Image
from pyzbar import pyzbar

img = Image.open('qr-code.png')
qr_output = pyzbar.decode(img)

print("qr-code.png decode:" )
print(qr_output)

img = Image.open('my_codelearn.png')
my_qr_output = pyzbar.decode(img)

print("my_codelearn.png decode:" )
print(my_qr_output)