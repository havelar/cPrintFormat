############# Simple printing #############
from cprint import cPrint

cPrint('Henrique ', 'red', end='')
cPrint('Avelar ', 'blue', end='')
cPrint('Amaral', 'pink')
    
############# Save format to be used anywhere #############
from cprint import cClass

red = cClass('red', 'white', style='bold', end='')
blue = cClass('blue', 'white', style='bold')
green = cClass('green')

red('Henrique ')
blue('Amaral')

############# Easy Success / Warning / Error printing #############
from cprint import cWarn, cSuccess, cError

cError('THIS SHOULD NEVER HAPPEN!!')
cWarn('Might not work, idk yet...')
cSuccess('Deu certo!')
