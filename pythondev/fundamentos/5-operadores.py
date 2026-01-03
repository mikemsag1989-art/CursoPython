num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

#Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print (f"Potencia do número {num1} por {num2} é: {exp}\n")
print (f"Soma do número {num1} por {num2} é: {sum}\n")

#Comparacao
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print (f"Os números {num1} e {num2} sao iguais? {equal}\n")
print (f"O número {num1} é maior ou igual a {num2}? {biggerEqual}")

#Atribuicao

num1 += 1  # num1 = num1 + 1
num1 -= 1  # num1 = num1 - 1
num1 *= 1  # num1 = num1 * 1
num1 /= 1  # num1 = num1 / 1

print (f"O novo valor de num1 agora é: {num1}")