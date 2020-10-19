class cFormat:
    colors = {
        'black': (0,0,0),
        'white': (255,255,255),
        'red': (255,0,0),
        'green': (0,200,0),
        'blue': (0,0,255),
        'yellow': (235,235,0),
        'purple': (128,0,128),
        'lilac': (158,92,186),
        'cyan': (0,255,255),
        'pink': (223, 60, 120),
        'brown': (121,53,19),
        'lime': (191, 255, 0),
        'orange': (255, 128, 0),
        'gray': (175, 175, 175),
        'light_blue': (32, 173, 233),
        'dark_blue': (0,0,85)
    }
    
    styles = {
        'normal': 2,
        'bold': 1,
        'underline': 4,
        'inverse': 7,
    }
    
    font_structure = '\x1B[38;2;{0};{1};{2};{3}m'# .format(R, G, B, style)
    bg_structure = '\x1B[48;2;{0};{1};{2}m' # .format(R, G, B)
    
    end = '\033[0m' # Return Font to original