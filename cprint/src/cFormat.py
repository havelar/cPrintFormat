class cFormat:
    colors = {
        'black': (0,0,0),
        'red': (255,0,0),
        'green': (0,200,0),
        'yellow': (235,235,0),
        'blue': (0,0,255),
        'purple': (128,0,128),
        'cyan': (0,255,255),
        'white': (255,255,255),
        'pink': (225, 162, 173),
        'brown': (160,82,45),
        'lime': (191, 255, 0),
        'orange': (255, 128, 0),
        'gray': (175, 175, 175)
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