num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ') 

numero1 = float(num1)
numero2 = float(num2)


if numero1 > numero2:
	print(f' o primeiro número: {numero1} é maior que o segundo número: {numero2}')
elif numero1 < numero2:
	print(f' o segundo número: {numero2} é maior que o primeiro número: {numero1}')
else:
	print('os números são iguais')