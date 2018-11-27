import barcode
from io import StringIO
from barcode import generate
from barcode.writer import ImageWriter

f2 = open('bar', 'wb')
generate('EAN13', u'5901234123457',output='line_2')
generate('EAN13', u'5901234123457', writer=ImageWriter(), output=f2)
generate('EAN13', u'5901234123457', writer=ImageWriter(), output='line')