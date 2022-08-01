'''
leia do teclado uma temperatura em graus Fahrenheit e mostre na tela o seu valor convertido em Celsius.
Lembrando que (c/5) = (f-32)/9. (Valores inválidos: menores que -457,69).
'''

grau_fahrenheit = -457.7
while grau_fahrenheit < -457.69:
    grau_fahrenheit = float(input('Insira um valor em graus Fahrenheit : \n'))

print(f'Valor convertido em Celsius = {(grau_fahrenheit-32)/1.8:.2f} graus.')
