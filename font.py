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
    # R = Right

    # 3rd character
    # R = Rounded
    # S = Square

    TILE_ULR = u'\u256D'
    TILE_URR = u'\u25DE'
    TILE_ULS = u'\u250C'
    TILE_URS = u'\u2510'

    TILE_MLS = u'\u251C'
    TILE_MRS = u'\u2524'

    TILE_LLR = u'\u2570'
    TILE_LRR = u'\u256F'
    TILE_LLS = u'\u2514'
    TILE_LRS = u'\u2518'

    TILE_BLANK = u' '
    TILE_HORI = u'\u2500'
    TILE_HORI_LHALF = u'\u2574'
    TILE_HORI_RHALF = u'\u2576'
    TILE_VERT = u'\u2502'
    TILE_VERT_UHALF = u'\u2575'
    TILE_VERT_LHALF = u'\u2577'

    # Numbers
    GLYPH_0 = [ [ TILE_ULS, TILE_URS ], [ TILE_VERT, TILE_VERT ], [ TILE_LLS, TILE_LRS ] ]
    GLYPH_1 = [ [ TILE_BLANK, TILE_VERT_LHALF ], [ TILE_BLANK, TILE_VERT ], [ TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_2 = [ [ TILE_HORI_RHALF, TILE_URS ], [ TILE_ULS, TILE_LRS ], [ TILE_LLS, TILE_HORI_LHALF ] ]
    GLYPH_3 = [ [ TILE_HORI_RHALF, TILE_URS ], [ TILE_HORI_RHALF, TILE_MRS ], [ TILE_HORI_RHALF, TILE_LRS ] ]
    GLYPH_4 = [ [ TILE_VERT_LHALF, TILE_VERT_LHALF ], [ TILE_LLS, TILE_MRS ], [ TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_5 = [ [ TILE_ULS, TILE_HORI_LHALF ], [ TILE_LLS, TILE_URS ], [ TILE_HORI_RHALF, TILE_LRS ] ]
    GLYPH_6 = [ [ TILE_ULS, TILE_HORI_LHALF ], [ TILE_MLS, TILE_URS ], [ TILE_LLS, TILE_LRS ] ]
    GLYPH_7 = [ [ TILE_HORI_RHALF, TILE_URS ], [ TILE_BLANK, TILE_VERT ], [ TILE_BLANK, TILE_VERT_UHALF ] ]
    GLYPH_8 = [ [ TILE_ULS, TILE_URS ], [ TILE_MLS, TILE_MRS ], [ TILE_LLS, TILE_LRS ] ]
    GLYPH_9 = [ [ TILE_ULS, TILE_URS ], [ TILE_LLS, TILE_MRS ], [ TILE_BLANK, TILE_VERT_UHALF ] ]


    def __init__(self, character):
        """
        Class to encapsulate a single character
        """
        self._glyph = []

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
