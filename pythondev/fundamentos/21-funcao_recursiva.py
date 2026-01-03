"""

fatorial de um numero:

1 -> 1 * 1 = 1
2 -> 2 * 1 = 2 * fatorial(1) = 2
3 -> 3 * 2 * 1  = 3 * fatorial(2) = 6
4 -> 4 * 3 * 2 * 1 = 4 * fatorial(3) = 24
5 -> 5 * 4 * 3 * 2 * 1 = 5 * fatorial(4) = 120

""" 

# 1 - funcao recursiva para calcular o fatorial de um numero
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

num = int(input("Digite um número para calcular o fatorial: \n"))
print(f"O fatorial de {num} é: {factorial(num)}")


# 2 - funcao recursiva para calcular a soma dos numeros de 1 ate n
def total_sum(num):
    if num == 1:
        return 1
    else:
        return num + total_sum(num - 1)

num = int(input("Digite um número para calcular a soma de 1 até n: \n"))
print(f"A soma dos números de 1 até {num} é: {total_sum(num)}")
