import math

a=int(input('digite um angulo: '))

sen=math.sin(math.radians(a))
cos=math.cos(math.radians(a))
tan=math.tan(math.radians(a))

print('aqui está seu valores do angulo {}: \nseno: {:.2f}\ncosseno: {:.2f}\ntangente:{:.2f}'.format(a,sen,cos,tan))