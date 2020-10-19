from .src.cFormat import cFormat

def cprint(txt, color='black', bg=None, style='normal', end='\n', returning=False):
        
    # Font Color process
    if isinstance(color,str):
        rgb = cFormat.colors.get(color.lower())
        if rgb is None:
            raise ValueError('Unkown color.')
    elif isinstance(color,tuple) and len(color)==3:
        rgb = color
    else:
        raise ValueError('Color must be string or (R,G,B). Not: {0}'.format(type(color)))
    
    curr_style = cFormat.styles.get(style.lower())
    if curr_style is None:
        raise ValueError("Invalid style value: '{0}' with type '{1}'".format(curr_style, type(curr_style)))
    prefix = cFormat.font_structure.format(*rgb, curr_style)

    # BackGround process
    if bg:
        if isinstance(bg,str):
            bg_rgb = cFormat.colors.get(bg.lower())
            if bg_rgb is None:
                raise ValueError('Unkown color.')
        elif isinstance(bg,tuple) and len(bg)==3:
            bg_rgb = bg
        else:
            raise ValueError('Color must be string or (R,G,B)')
    if bg:
        prefix = prefix + cFormat.bg_structure.format(*bg_rgb)

    string = prefix + str(txt) + cFormat.end

    if returning: # Return formated string to be used anywhere
        return string
    else: # Just print
        print(string, end=end)