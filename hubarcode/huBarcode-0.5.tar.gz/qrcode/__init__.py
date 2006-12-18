#!/usr/bin/env python

"""QR Code encoder

All needed by the user is done via the QRCodeEncoder class:

>>> encoder = QRCodeEncoder("HuDoRa")
>>> # encoder.save( "test.png" )
>>> print encoder.get_ascii()

"""

__revision__ = "$Rev: 53 $"

from qrcode.textencoder import TextEncoder
from qrcode.renderer import QRCodeRenderer

class QRCodeEncoder:
    """Top-level class which handles the overall process of
    encoding input data, placing it in the matrix and
    outputting the result"""

    def __init__(self, text, ecl=None):
        """Set up the encoder with the input text.
        This will encode the text,
        and create a matrix with the resulting codewords"""

        enc = TextEncoder()
        self.matrix = enc.encode(text, ecl)
    # end def __init__


    def save(self, filename, cellsize=5):
        """Write the matrix out to an image file"""

        qrc = QRCodeRenderer(self.matrix)
        qrc.write_file(cellsize, filename)
    # end def save


    def get_ascii(self):
        """Return an ascii representation of the matrix"""
        qrc = QRCodeRenderer(self.matrix)
        return qrc.get_ascii()
    # end def get_ascii
# end class QRCodeEncoder

