import qrcode

img = qrcode.make('https://youtu.be/uhmJ9erFU8E')
img.save('qr_code.png')