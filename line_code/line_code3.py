import barcode
from io import BytesIO
from barcode import generate
from barcode.writer import ImageWriter

fp = BytesIO()

f1 = open('barcode_svg1', 'wb')
f2 = open('barcode_svg2', 'wb')


name1 = generate('EAN13', u'5901234123457', output=fp)
name1 = generate('EAN13', u'5901234123457', output=f2)

name2 = generate('EAN13', u'5901234123457', output='barcode_svg')
name2 = generate('EAN13', u'5901234123457', output=f2)