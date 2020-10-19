############# Simple printing #############
from cprint import cPrint
print(1*'\n'+'############# Testing Simple printing #############\n')

cPrint('Henrique em vermelho', 'red')
cPrint('Avelar Bold Blue', 'blue', style='underline')
cPrint('Amaral subline', 'pink', style='bold')
    
############# Save format to be used anywhere #############
from cprint import cClass
print(3*'\n'+'############# Testing saved format #############\n')

red = cClass('red', 'white', style='bold', end=' | ')
blue = cClass('blue', 'white', style='bold', end=' | ')
green = cClass('green')

red('Henrique ')
blue('Avelar')
green('Amaral')

############# Easy Success / Warning / Error printing #############
from cprint import cWarn, cSuccess, cError
print(3*'\n'+'############# Testing warnings #############\n')

cSuccess('Worked.')
cWarn('Might not work, idk yet...')
cError('This is an error !!')

############# Printing Script #############
from cprint import cScript
print(3*'\n'+'############# Testing script #############\n')

script = "<script>\n$(document).ready(function() {\n  let src  = parseInt('{URLPARAMETERS_source}');\n  if (src == '0') {\n    $('input.text:visible').val('Offerwise');\n  } else {\n    $('input.text:visible').val('Unkown source.');\n  }\n  $('#movenextbtn').click();\n});\n</script>"
cScript(script, 'black', 'gray', style='bold')

############# Multi Colored #############
from cprint import cColor
print(3*'\n'+'############# Testing Multi Colored #############\n')

print(cColor('Henrique','red', style='bold') +'-'+ cColor('Avelar', 'green', style='bold') +'-'+ cColor('Amaral', 'blue', style='bold'))
