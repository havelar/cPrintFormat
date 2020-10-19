import inspect

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

    if not module is None: # In some cases like Notebook inspect cannot find where file is located.
        filename = module.__file__
        line = frame.lineno

        file_text = ' Success at {0}: {1} '.format(filename, line)
    else:
        file_text = 'Success !'
    cPrint(text=file_text, color=(17, 70, 29), bg=(96, 222, 125), style='bold')

    cPrint(start = '\t-> ', text=text, color=(63, 125, 78), style='bold')


def cError(text):
    '''
        Print text in error format.
    '''

    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    if not module is None: # In some cases like Notebook inspect cannot find where file is located.
        filename = module.__file__
        line = frame.lineno
        file_text = ' Error at {0}: {1} '.format(filename, line)
    else:
        file_text = 'Error !'

    cPrint(text=file_text, color=(110, 0, 0), bg=(255, 50, 50), style='bold')

    cPrint(start = '\t-> ', text=text, color=(229, 42, 42), style='bold')


def cWarn(text):
    '''
        Print text in warning format.
    '''

    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    if not module is None: # In some cases like Notebook inspect cannot find where file is located.
        filename = module.__file__
        line = frame.lineno
        file_text = ' Warning at {0}: {1} '.format(filename, line)
    else:
        file_text = 'Warning !'

    cPrint(text=file_text, color=(40, 40, 40), bg=(238, 243, 81), style='bold')

    cPrint(start = '\t-> ', text=text, color=(205, 222, 96), style='bold')


############################ Script Formats ############################

def cScript(script, color='gray', bg=None, style='normal'):
    '''
        Print formated Scripts with line numbered.
    '''
    script_lines = script.split('\n')
    lenght = len(str(len(script_lines))) # Script lenght

    for ind, line in enumerate(script_lines):
        ind = str(ind) # Convert to STR
        if len(ind) < lenght: # Code to add '0' so every line is same size
            dec = lenght - len(ind) # Complete decimals
            ind = (dec*'0') + str(ind) # 5 -> 005 if script len is > 100
        cprint(ind + '-| ' + line, color, bg, style)


############################ Multi Color ############################

def cColor(text, color='black', bg=None, style='normal'):
    '''
        Kind same as cPrint, but instead of printing, text is returned so can be appended at other strings
        to print only one word with selected format.
    '''
    return cprint(text, color=color, bg=bg, style=style, end='', returning=True)