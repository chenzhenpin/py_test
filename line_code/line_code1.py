import barcode
from io import StringIO
from barcode import generate
from barcode.writer import ImageWriter
EAN = barcode.get_barcode_class('ean13')
ean = EAN(u'5901234123334', writer=ImageWriter())
fullname = ean.save('ean13_barcode')