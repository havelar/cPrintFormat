from . import cprint

class cPrintClass:
    def __init__(self, color='black', bg=None, style='normal', end='\n'):
        self.__color = color
        self.__bg = bg
        self.__style = style
        self.__end = end

    def print_format(self, text):
        cprint(text, color=self.__color, bg=self.__bg, style=self.__style, end=self.__end)