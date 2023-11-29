h=float(input('qual a altura da parede?: '))
l=float(input('e a largura?: '))
print(''*30)
print('vejamos...')
print(''*30)
a=h*l
mc=a/2
print('sua àrea é de {}m² '
      '\nportanto, vão ser necessário {:.0f}l de tinta para pintar a parede'.format(a,mc))
