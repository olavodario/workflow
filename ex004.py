x = input('Digite qualquer coisa; ')

print (f'Tipo do que foi digitado: {type(x)}')
print ('Só tem espaços? {}' .format (x.isspace()))
print (f'O que foi digitado é numérico? {x.isnumeric()}')
print ('É alphanumerico?{}' .format(x.isalnum()))
print (f'O que foi digitado é decimal? {x.isdecimal()}')
print (f'O que foi digitado  está em minusculos? {x.islower()}')
print (f'O que foi digitado  está em maiusculas? {x.upper()}')
print (f'Está capitalizado? {x.istitle()}')