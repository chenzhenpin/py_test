import qrcode
 
img = qrcode.make('http://onlysee.6655.la')
# img <qrcode.image.pil.PilImage object at 0x1044ed9d0>
 
with open('dian.png', 'wb') as f:
    img.save(f)