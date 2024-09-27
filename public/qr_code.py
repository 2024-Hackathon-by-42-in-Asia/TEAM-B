import qrcode

img = qrcode.make('https://tinyurl.com/yu37krka')
img.save('qr_code_3.png')