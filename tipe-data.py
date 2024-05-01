print('##  program poython konversisuhu  ##') 
print('===================================')
print()

celc = float(input('Input suhu celsius: '))

fahr = (9/5 * celc) + 32
kelv = celc + 273.15
ream = celc * (4/5)

print(celc,'derajat celsius =',fahr,'derajat Fahrenheit')
print(celc,'derajat celsius =',kelv,'derajat kelvin')
print(celc,'derajat celsius =',ream,'derajat reamur')
