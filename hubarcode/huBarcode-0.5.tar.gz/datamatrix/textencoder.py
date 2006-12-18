"""Text encoder for 2D datamatrix barcode encoder"""

__revision__ = "$Rev: 53 $"

import sys
from reedsolomon import get_reed_solomon_code
import logging

log = logging.getLogger("datamatrix")

data_word_length = ( 3, 5, 8, 12,  18,  22,   30,   36,  44, 
                     62,  86, 114,  144,  174, 204, 
                     280, 368, 456,  576,  696, 816, 
                     1050, 1304, 1558 )

error_word_length = ( 5, 7, 10, 12,  14,  18,  20,  24,  28, 
                      36,  42,  48,  56,  68,  84,
                      112, 144, 192, 224, 272, 336,
                      408, 496, 620 )

data_region_size = (  8, 10, 12, 14, 16, 18, 20, 22, 24,
                                 14, 16, 18, 20, 22, 24,
                                 14, 16, 18, 20, 22, 24,
                                         18, 20, 22 )

class TextEncoder:
    """Text encoder class for 2D datamatrix"""

    def __init__( self ):
        self.codewords = ''
        self.size_index = None
        self.mtx_size = 0

    def encode( self, text ):
        """Encode the given text and add padding and error codes
        also set up the correct matrix size for the resulting codewords"""

        self.__init__( )

        self.encode_text( text )

        self.pad( )

        self.append_error_codes( )

        log.debug( "Codewords: " + 
                ' '.join( [str(ord(codeword)) for codeword in self.codewords] ) )

        self.mtx_size = data_region_size[self.size_index]

        log.debug( "Matrix size will be %d", self.mtx_size )

        return self.codewords

        
    
    def encode_text( self, text ):
        """Encode the given text into codewords"""

        numbuf = ''

        for char in text:
            if char.isdigit():
                numbuf += char
                if len(numbuf) == 2:
                    # we have collected two numbers: add them as a digit pair
                    self.append_digits(numbuf)
                    numbuf = '' 
            else:
                if numbuf:
                    # an unpaired number: add it as an ascii character
                    self.append_ascii_char( numbuf )
                    numbuf = ''

                # a regular ascii character
                self.append_ascii_char( char )

        # there might be a single number left over at the end
        if numbuf: 
            self.append_ascii_char( numbuf )



    def pad( self ):
        """Pad out the encoded text to the correct word length"""
        
        unpadded_len = len(self.codewords)
        log.debug( "Unpadded data size:   %d bytes", unpadded_len )

        # Work out how big the matrix needs to be
        for self.size_index, length in enumerate(data_word_length):
            if length >= unpadded_len: 
                break

        if self.size_index > 8:
            log.error( "Data too big" )
            sys.exit(0)

        # Number of characters with which the data will be padded
        padsize = length - unpadded_len

        log.debug( "Pad size: %d bytes", padsize )

        # First pad character is 129
        if padsize:
            self.codewords += chr(129)

        def rand253( pos ):
            """generate the next padding character""" 
            rnd = ((149 * pos) % 253) + 1
            return (129 + rnd) % 254    
        
        # Remaining pad characters generated by 253-state algorithm
        for i in range( 1, padsize ):
            self.codewords += chr(rand253( unpadded_len+i+1 ))

        log.debug( "Word size after padding: %d bytes", len(self.codewords) )

    
    def append_error_codes( self ):
        """Calculate the necessary number of Reed Solomon error codes for the
        encoded text and padding codewords, and append to the codeword buffer"""

        error_length = error_word_length[self.size_index]
        log.debug( "Error word length: %d bytes", error_length )

        error_words = get_reed_solomon_code( self.codewords, error_length )

        self.codewords += error_words


    def append_digits( self, digits ):
        """Write a pair of digits
        (the appended value is 130 + the integer value of the digits together"""

        append = chr(130+int(digits))
        self.codewords += append
        log.debug( 'digits:  "%s" ==> %s', digits, ord(append) )

                
    def append_ascii_char( self, char ):
        """Append a single ascii character
        (the appended value is the value of the char plus 1"""
        
        append = chr(ord(char)+1)
        self.codewords += append
        log.debug( 'ascii:   "%c" ==> %d', char, ord(append) )

