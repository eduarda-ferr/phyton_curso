import random
print('-_'*30)
n1=input('primeiro nome: ')
n2=input('segundo nome: ')
n3=input('terceiro nome: ')
n4=input('quarto nome: ')
n5=input('quinto nome: ')

lista=[n1,n2,n3,n4,n5]
#funçao len()=comprimento da lista nunca esquecer disto!!!
#reorganizacao=random.sample(lista,len(lista))

random.shuffle(lista)


print('-_'*30)
print(f'a nova organização da lista para a apresentaçao:\n{lista} ')




