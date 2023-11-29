import random

aluno1=input('nome do primeiro aluno: ')
aluno2=input('nome do segundo aluno: ')
aluno3=input('nome do terceiro aluno: ')
aluno4=input('nome do quarto aluno: ')
aluno5=input('nome do quinto aluno: ')

lista=[aluno1,aluno2,aluno3,aluno4,aluno5]

escolhido=random.choice(lista)

print(f'O aluno escolhido foi {escolhido}, parabéns :0')