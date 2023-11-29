km=float(input('quantos quilometros este carro percorreu?:'))
d=float(input('em quantos dias?: '))

c=(60*d)

h=(km*0.15)

r=c+h

print('_'*30)
print('calculando...')
print('_'*30)

print('O Valor de acordo com {:.0f} dias e {:.0f}km percorridos, é de R${:.2f}'.format(d,km,r))
