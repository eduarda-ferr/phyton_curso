s=float(input('digite o valor: R$'))
print('calculando...')

p=(15*s)/100
a=s+p
print('='*60)
print('o valor do salário de R${} teve aumento de 15%(R${}),\n'
      'no qual, o valor final é de R${}'.format(s,p,a))
print('='*60)