#Exercício 6 - Ler temperatura em graus Celsius e converter para Kelvin
print('Digite a temperatura em graus Celsius:')
celsius = float(input())
kelvin = round((celsius+273.15),1)
#o resultado será exibido com a limitação de 1 casa decimal
print(f'Neste momento {kelvin} graus Kelvin')