medida=float(input('mostre o valor em metros: '))
print('convertendo o valor em km,hm,dam - dm, cm e mm')
km=medida/1000
hm=medida/100
dam=medida/10
dm=medida*10
cm=medida*100
mm=medida*1000
print('{} metro(s) corresponde à:\n{} em km \n{} em hm \n{} em dam \n{} em dm \n{} em cm \n{} em mm'.format(medida,km,hm,dam,dm,cm,mm))
