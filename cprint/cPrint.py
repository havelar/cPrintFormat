from .src.cFormat import cFormat

def cprint(txt, color='black', bg=None, style='normal', end='\n'):
        
    # Font Color process
    if isinstance(color,str):
        rgb = cFormat.colors.get(color)
        if rgb is None:
            raise ValueError('Unkown color.')
    elif isinstance(color,tuple) and len(color)==3:
        rgb = color
    else:
        raise ValueError('Color must be string or (R,G,B)')
    prefix = cFormat.font_structure.format(*rgb, cFormat.styles[style])

    # BackGround process
    if bg:
        if isinstance(bg,str):
            bg_rgb = cFormat.colors.get(bg)
            if bg_rgb is None:
                raise ValueError('Unkown color.')
        elif isinstance(bg,tuple) and len(bg)==3:
            bg_rgb = bg
        else:
            raise ValueError('Color must be string or (R,G,B)')
    if bg:
        prefix = prefix + cFormat.bg_structure.format(*bg_rgb)

    
    string = prefix + str(txt) + cFormat.end
    print(string, end=end)