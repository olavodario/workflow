from random import randint
from time import sleep
import emoji

a = randint(0,5)
print('-=-'*20)
r = input('Vamos Jogar um jogo?(S/N) ').strip().upper()
print('-=-'*20)

if r == 'S' or r == 'SIM':
    print('Vou pensar em um número tente adivinhar🤓!')
    print('PROCESSANDO...')
    sleep(3)
    n = int(input('Me fale um número de 1 a 5: '))
    if n == a:
        print(emoji.emojize('PARABENS!!! VOCÊ VENCEU! :beaming_face_with_smiling_eyes:'))
    else:
        print(emoji.emojize('VENCI! Eu pensei no número {}... O mundo será dominado!:loudly_crying_face:'.format(a)))
else:
    print(emoji.emojize('Que pena...Fica para proxima então! :angry_face_with_horns:'))




