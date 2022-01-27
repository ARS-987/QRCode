# pip install qrcode
# pip install pillow

import qrcode
date = 'ARS-987'
qr = qrcode.QRCode(version=1 , box_size=10 , border=5)
qr.add_data(date)
qr.make(fit = True)
img = qr.make_image(fill_color = 'red', back_color = 'white')
img.save('MyQRCode.png')

# py QRCode.py