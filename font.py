#!/usr/bin/env python3
"""
Sizeable font for text displays

Provides a sizeable font for text terminals using the box drawing characters
"""

###############################################################################
class Glyph:
###############################################################################
    """
    Contains the data for a single character
    """

    # 1st character
    # U = Upper
    # M = Middle
    # L = Lower

    # 2nd character
    # L = Left
    # M = Middle
    # R = Right

    # 3rd character
    # R = Rounded
    # S = Square

    TILE_ULR = u'\u256D'
    TILE_ULS = u'\u250C'
    TILE_UMS = u'\u252C'
    TILE_URR = u'\u256E'
    TILE_URS = u'\u2510'

    TILE_MLS = u'\u251C'
    TILE_MRS = u'\u2524'

    TILE_LLR = u'\u2570'
    TILE_LLS = u'\u2514'
    TILE_LMS = u'\u2534'
    TILE_LRR = u'\u256F'
    TILE_LRS = u'\u2518'

    TILE_BLANK = u' '
    TILE_HORI = u'\u2500'
    TILE_HORI_LHALF = u'\u2574'
    TILE_HORI_RHALF = u'\u2576'
    TILE_VERT = u'\u2502'
    TILE_VERT_UHALF = u'\u2575'
    TILE_VERT_LHALF = u'\u2577'

    TILE_X = u'\u2573'
    TILE_BSLASH = u'\u2572'
    TILE_FSLASH = u'\u2571'

    TILE_DOT_UL = u'\u2598'
    TILE_DOT_UR = u'\u259D'
    TILE_DOT_LL = u'\u2596'
    TILE_DOT_LR = u'\u2597'

    # Symbols
    GLYPH_SPACE = [ [ TILE_BLANK, TILE_BLANK, TILE_BLANK ], [ TILE_BLANK, TILE_BLANK, TILE_BLANK ], [ TILE_BLANK, TILE_BLANK, TILE_BLANK ] ]
    GLYPH_PERIOD = [ [ TILE_BLANK, TILE_BLANK, TILE_BLANK ], [ TILE_BLANK, TILE_BLANK, TILE_BLANK ], [ TILE_BLANK, TILE_BLANK, TILE_DOT_UL ] ]
    GLYPH_COLON = [ [ TILE_BLANK, TILE_DOT_LL, TILE_BLANK ], [ TILE_BLANK, TILE_BLANK, TILE_BLANK ], [ TILE_BLANK, TILE_DOT_UL, TILE_BLANK ] ]

    # Numbers
    GLYPH_0 = [ [ TILE_ULS, TILE_HORI, TILE_URS ], [ TILE_VERT, TILE_FSLASH, TILE_VERT ], [ TILE_LLS, TILE_HORI, TILE_LRS ] ]
    GLYPH_1 = [ [ TILE_HORI_RHALF, TILE_URS, TILE_BLANK ], [ TILE_BLANK, TILE_VERT, TILE_BLANK ], [ TILE_HORI_RHALF, TILE_LMS, TILE_HORI_LHALF ] ]
    GLYPH_2 = [ [ TILE_HORI_RHALF, TILE_HORI, TILE_URS ], [ TILE_ULS, TILE_HORI, TILE_LRS ], [ TILE_LLS, TILE_HORI, TILE_HORI_LHALF ] ]
    GLYPH_3 = [ [ TILE_HORI_RHALF, TILE_HORI, TILE_URS ], [ TILE_HORI_RHALF, TILE_HORI, TILE_MRS ], [ TILE_HORI_RHALF, TILE_HORI, TILE_LRS ] ]
    GLYPH_4 = [ [ TILE_VERT_LHALF, TILE_BLANK, TILE_VERT_LHALF ], [ TILE_LLS, TILE_HORI, TILE_MRS ], [ TILE_BLANK, TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_5 = [ [ TILE_ULS, TILE_HORI, TILE_HORI_LHALF ], [ TILE_LLS, TILE_HORI, TILE_URS ], [ TILE_HORI_RHALF, TILE_HORI, TILE_LRS ] ]
    GLYPH_6 = [ [ TILE_ULS, TILE_HORI, TILE_HORI_LHALF ], [ TILE_MLS, TILE_HORI, TILE_URS ], [ TILE_LLS, TILE_HORI, TILE_LRS ] ]
    GLYPH_7 = [ [ TILE_HORI_RHALF, TILE_HORI, TILE_URS ], [ TILE_BLANK, TILE_BLANK, TILE_VERT ], [ TILE_BLANK, TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_8 = [ [ TILE_ULS, TILE_HORI, TILE_URS ], [ TILE_MLS, TILE_HORI, TILE_MRS ], [ TILE_LLS, TILE_HORI, TILE_LRS ] ]
    GLYPH_9 = [ [ TILE_ULS, TILE_HORI, TILE_URS ], [ TILE_LLS, TILE_HORI, TILE_MRS ], [ TILE_BLANK, TILE_BLANK, TILE_VERT_UHALF ] ]

    # Uppercase
    GLYPH_A = [ [ TILE_ULR, TILE_HORI, TILE_URR ], [ TILE_MLS, TILE_HORI, TILE_MRS ], [ TILE_VERT_UHALF, TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_B = [ [ TILE_ULS, TILE_HORI, TILE_URR ], [ TILE_MLS, TILE_HORI, TILE_MRS ], [ TILE_LLS, TILE_HORI, TILE_LRR ] ]
    GLYPH_C = [ [ TILE_ULR, TILE_HORI, TILE_HORI_LHALF ], [ TILE_VERT, TILE_BLANK, TILE_BLANK ], [ TILE_LLR, TILE_HORI, TILE_HORI_LHALF ] ]
    GLYPH_D = [ [ TILE_ULS, TILE_HORI, TILE_URR ], [ TILE_VERT, TILE_BLANK, TILE_VERT ], [ TILE_LLS, TILE_HORI, TILE_LRR ] ]
    GLYPH_E = [ [ TILE_ULS, TILE_HORI, TILE_HORI_LHALF ], [ TILE_MLS, TILE_HORI, TILE_HORI_LHALF ], [ TILE_LLS, TILE_HORI, TILE_HORI_LHALF ] ]
    GLYPH_F = [ [ TILE_ULS, TILE_HORI, TILE_HORI_LHALF ], [ TILE_MLS, TILE_HORI, TILE_HORI_LHALF ], [ TILE_VERT_UHALF, TILE_BLANK, TILE_BLANK ] ]
    GLYPH_G = [ [ TILE_ULR, TILE_HORI, TILE_HORI_LHALF ], [ TILE_VERT, TILE_BLANK, TILE_URS ], [ TILE_LLR, TILE_HORI, TILE_LRR ] ]
    GLYPH_H = [ [ TILE_VERT_LHALF, TILE_BLANK, TILE_VERT_LHALF ], [ TILE_MLS, TILE_HORI, TILE_MRS ], [ TILE_VERT_UHALF, TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_I = [ [ TILE_HORI_RHALF, TILE_UMS, TILE_HORI_LHALF ], [ TILE_BLANK, TILE_VERT, TILE_BLANK ], [ TILE_HORI_RHALF, TILE_LMS, TILE_HORI_LHALF ] ]
    GLYPH_J = [ [ TILE_HORI_RHALF, TILE_HORI, TILE_URR ], [ TILE_VERT_LHALF, TILE_BLANK, TILE_VERT ], [ TILE_LLR, TILE_HORI, TILE_LRR ] ]
    GLYPH_K = [ [ TILE_VERT_LHALF, TILE_ULR, TILE_BLANK ], [ TILE_MLS, TILE_LMS, TILE_URR ], [ TILE_VERT_UHALF, TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_L = [ [ TILE_VERT_LHALF, TILE_BLANK, TILE_BLANK ], [ TILE_VERT, TILE_BLANK, TILE_BLANK ], [ TILE_LLS, TILE_HORI, TILE_HORI_LHALF ] ]
    GLYPH_M = [ [ TILE_ULS, TILE_UMS, TILE_URS ], [ TILE_VERT, TILE_VERT, TILE_VERT ], [ TILE_VERT_UHALF, TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_N = [ [ TILE_VERT_LHALF, TILE_BLANK, TILE_VERT_LHALF ], [ TILE_VERT, TILE_BSLASH, TILE_VERT ], [ TILE_VERT_UHALF, TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_O = [ [ TILE_ULR, TILE_HORI, TILE_URR ], [ TILE_VERT, TILE_BLANK, TILE_VERT ], [ TILE_LLR, TILE_HORI, TILE_LRR ] ]
    GLYPH_P = [ [ TILE_ULS, TILE_HORI, TILE_URR ], [ TILE_MLS, TILE_HORI, TILE_LRR ], [ TILE_VERT_UHALF, TILE_BLANK, TILE_BLANK ] ]
    GLYPH_Q = [ [ TILE_ULR, TILE_HORI, TILE_URR ], [ TILE_VERT, TILE_BSLASH, TILE_VERT ], [ TILE_LLR, TILE_HORI, TILE_LRR ] ]
    GLYPH_R = [ [ TILE_ULS, TILE_URR, TILE_BLANK ], [ TILE_MLS, TILE_LMS, TILE_URR ], [ TILE_VERT_UHALF, TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_S = [ [ TILE_ULR, TILE_HORI, TILE_HORI_LHALF ], [ TILE_LLR, TILE_HORI, TILE_URR ], [ TILE_HORI_RHALF, TILE_HORI, TILE_LRR ] ]
    GLYPH_T = [ [ TILE_HORI_RHALF, TILE_UMS, TILE_HORI_LHALF ], [ TILE_BLANK, TILE_VERT, TILE_BLANK ], [ TILE_BLANK, TILE_VERT_UHALF, TILE_BLANK ] ]
    GLYPH_U = [ [ TILE_VERT_LHALF, TILE_BLANK, TILE_VERT_LHALF ], [ TILE_VERT, TILE_BLANK, TILE_VERT ], [ TILE_LLR, TILE_HORI, TILE_LRR ] ]

    GLYPH_V = [ [ TILE_VERT_LHALF, TILE_BLANK, TILE_BLANK, TILE_VERT_LHALF ], [ TILE_LLR, TILE_BLANK, TILE_BLANK, TILE_LRR ], [ TILE_BLANK, TILE_LLR, TILE_LRR, TILE_BLANK ] ]

    GLYPH_W = [ [ TILE_VERT_LHALF, TILE_BLANK, TILE_VERT_LHALF ], [ TILE_VERT, TILE_VERT, TILE_VERT ], [ TILE_LLS, TILE_LMS, TILE_LRS ] ]
    GLYPH_X = [ [ TILE_BSLASH, TILE_BLANK, TILE_FSLASH ], [ TILE_BLANK, TILE_X, TILE_BLANK ], [ TILE_FSLASH, TILE_BLANK, TILE_BSLASH ] ]
    GLYPH_Y = [ [ TILE_VERT_LHALF, TILE_BLANK, TILE_VERT_LHALF ], [ TILE_LLR, TILE_UMS, TILE_LRR ], [ TILE_BLANK, TILE_VERT_UHALF, TILE_BLANK ] ]
    GLYPH_Z = [ [ TILE_HORI_RHALF, TILE_HORI, TILE_HORI_LHALF ], [ TILE_BLANK, TILE_FSLASH, TILE_BLANK ], [ TILE_HORI_RHALF, TILE_HORI, TILE_HORI_LHALF ] ]

    def __init__(self, character):
        """
        Class to encapsulate a single character
        """
        self._glyph = []

        if character == ' ':
            self._glyph = self._create(self.GLYPH_SPACE)
        if character == '.':
            self._glyph = self._create(self.GLYPH_PERIOD)
        if character == ':':
            self._glyph = self._create(self.GLYPH_COLON)

        if character == '0':
            self._glyph = self._create(self.GLYPH_0)
        if character == '1':
            self._glyph = self._create(self.GLYPH_1)
        if character == '2':
            self._glyph = self._create(self.GLYPH_2)
        if character == '3':
            self._glyph = self._create(self.GLYPH_3)
        if character == '4':
            self._glyph = self._create(self.GLYPH_4)
        if character == '5':
            self._glyph = self._create(self.GLYPH_5)
        if character == '6':
            self._glyph = self._create(self.GLYPH_6)
        if character == '7':
            self._glyph = self._create(self.GLYPH_7)
        if character == '8':
            self._glyph = self._create(self.GLYPH_8)
        if character == '9':
            self._glyph = self._create(self.GLYPH_9)

        if character == 'A':
            self._glyph = self._create(self.GLYPH_A)
        if character == 'B':
            self._glyph = self._create(self.GLYPH_B)
        if character == 'C':
            self._glyph = self._create(self.GLYPH_C)
        if character == 'D':
            self._glyph = self._create(self.GLYPH_D)
        if character == 'E':
            self._glyph = self._create(self.GLYPH_E)
        if character == 'F':
            self._glyph = self._create(self.GLYPH_F)
        if character == 'G':
            self._glyph = self._create(self.GLYPH_G)
        if character == 'H':
            self._glyph = self._create(self.GLYPH_H)
        if character == 'I':
            self._glyph = self._create(self.GLYPH_I)
        if character == 'J':
            self._glyph = self._create(self.GLYPH_J)
        if character == 'K':
            self._glyph = self._create(self.GLYPH_K)
        if character == 'L':
            self._glyph = self._create(self.GLYPH_L)
        if character == 'M':
            self._glyph = self._create(self.GLYPH_M)
        if character == 'N':
            self._glyph = self._create(self.GLYPH_N)
        if character == 'O':
            self._glyph = self._create(self.GLYPH_O)
        if character == 'P':
            self._glyph = self._create(self.GLYPH_P)
        if character == 'Q':
            self._glyph = self._create(self.GLYPH_Q)
        if character == 'R':
            self._glyph = self._create(self.GLYPH_R)
        if character == 'S':
            self._glyph = self._create(self.GLYPH_S)
        if character == 'T':
            self._glyph = self._create(self.GLYPH_T)
        if character == 'U':
            self._glyph = self._create(self.GLYPH_U)
        if character == 'V':
            self._glyph = self._create(self.GLYPH_V)
        if character == 'W':
            self._glyph = self._create(self.GLYPH_W)
        if character == 'X':
            self._glyph = self._create(self.GLYPH_X)
        if character == 'Y':
            self._glyph = self._create(self.GLYPH_Y)
        if character == 'Z':
            self._glyph = self._create(self.GLYPH_Z)


    def _create(self, prototype):
        """
        Concatenate glyph components together
        """
        glyph = []
        for row in prototype:
            tmp_row = u"".join(row)
            glyph.append(tmp_row)

        return glyph

    def __str__(self):
        rtn = u""
        for row in self._glyph:
            if len(rtn) > 0:
                rtn += u"\n"
            for cell in row:
                rtn += cell
        return rtn

    def get_data(self):
        return self._glyph

    def get_height(self):
        return len(self._glyph)

###############################################################################
class Font:
###############################################################################
    """
    Render text using the box characters
    """

    character_width = 3

    @staticmethod
    def render_string(string):
        """
        Convert the given string in to the equivalent box character glyphs
        """
        rtn = []

        if len(string) > 0:
            glyphs = []
            # Convert characters to glyphs
            for char in string:
                glyphs.append(Glyph(char))

            # Generate string by concating each row of the glyphs
            for i in range(0, glyphs[0].get_height()):
                rtn_row = u""
                for glyph in glyphs:
                    rtn_row += glyph.get_data()[i]
                rtn.append(rtn_row)

        return rtn

# Main
###############################################################################
if __name__ == '__main__':

#    g = Glyph('8')
#    print(g)

    fdata = Font.render_string("0123456789")
    for frow in fdata:
        print(frow)

    fdata = Font.render_string("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
    for frow in fdata:
        print(frow)

#    fdata = Font.render_string("abcdefghijklmnopqrstuvwxyz")
#    for frow in fdata:
#        print(frow)

    fdata = Font.render_string(":.")
    for frow in fdata:
        print(frow)
