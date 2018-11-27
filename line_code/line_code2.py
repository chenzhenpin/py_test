import barcode
from io import BytesIO
from barcode import generate
from barcode.writer import ImageWriter
EAN = barcode.get_barcode_class('ean13')
ean = EAN(u'5901234123457')
fp = BytesIO()
ean.write(fp)
f = open('file_wb', 'wb')
ean.write(f) # PIL (ImageWriter) produces RAW format here
