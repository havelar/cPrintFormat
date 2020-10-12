import inspect, re, json

from .cPrint import cprint
from .cClass import cPrintClass

indent_json = lambda _json: json.dumps(_json, indent=4, sort_keys=True)

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

#pattern = re.compile(r'\(\{(.*?)\}\)')
def cPrint(text, color='black', bg=None, style='normal', end='\n', start=None):
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
    if not start is None:
        cprint(start, color, bg, style, end='')
    
    cprint(text, color, bg, style, end)



############################ Warning Formats ############################

def cSuccess(text):
    '''
        Print text in success format.
    '''

    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    filename = module.__file__
    line = frame.lineno

    file_text = ' Success at {0}: {1} '.format(filename, line)
    cPrint(text=file_text, color=(17, 70, 29), bg=(96, 222, 125), style='bold')

    cPrint(start = '\t-> ', text=text, color=(63, 125, 78), style='bold')


def cError(text):
    '''
        Print text in error format.
    '''

    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    filename = module.__file__
    line = frame.lineno

    file_text = ' Error at {0}: {1} '.format(filename, line)
    cPrint(text=file_text, color=(110, 0, 0), bg=(255, 50, 50), style='bold')

    cPrint(start = '\t-> ', text=text, color=(229, 42, 42), style='bold')


def cWarn(text):
    '''
        Print text in warning format.
    '''

    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    filename = module.__file__
    line = frame.lineno

    file_text = ' Warning at {0}: {1} '.format(filename, line)
    cPrint(text=file_text, color=(40, 40, 40), bg=(238, 243, 81), style='bold')

    cPrint(start = '\t-> ', text=text, color=(205, 222, 96), style='bold')
