from .cPrint import cprint
from .cClass import cPrintClass

def cClass(color='black', bg=None, style='normal', end='\n'):
    '''
        Return a function to print with setted format.

        -> color: Font Color. String or (R, G, B) of integers.

        -> bg: BackGround Color. String or (R, G, B) of integers.

        -> style: Font Style. Possible styles:
            -> normal, bold, underline, inverse.
        
        -> end: End of string (Last caracter)

        -> Pre programmed colors:
            -> white, black, red, green, yellow, blue, purple, cyan, pink, brown, lime, orange, gray.
    '''
    return cPrintClass(color, bg, style, end).print_format

def cPrint(text, color='black', bg=None, style='normal', end='\n'):
    '''
        Print text with setted format.

        -> text: Text to be printed.

        -> color: Font Color. String or (R, G, B) of integers.

        -> bg: BackGround Color. String or (R, G, B) of integers.

        -> style: Font Style. Possible styles:
            -> normal, bold, underline, inverse.
        
        -> end: End of string (Last caracter)

        -> Pre programmed colors:
            -> white, black, red, green, yellow, blue, purple, cyan, pink, brown, lime, orange, gray.
    '''
    cprint(text, color, bg, style, end)