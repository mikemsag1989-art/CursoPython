# # infomacoes sobre o filme
# name = input("Digite o nome do filme: \n")
# year = int(input("Digite o ano do filme: \n"))  
# rating = float(input("Digite a avaliação do filme (0.0 a 10.0): \n"))

# # verifica se a avaliação é recomendada
# if rating >= 8.0 and year > 2015:
#     print(f"O filme {name} é recomendado.")
# else:
#     print(f"O filme {name} não é recomendado.")



# calculadora
num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))

operation = input("Digite a operação (+, -, *, /): \n")

if operation == "+":
    result = num1 + num2
    print(f"O resultado de {num1} + {num2} é {result}.")    
elif operation == "-":
    result = num1 - num2
    print(f"O resultado de {num1} - {num2} é {result}.")        
elif operation == "*":
    result = num1 * num2
    print(f"O resultado de {num1} * {num2} é {result}.")            
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"O resultado de {num1} / {num2} é {result}.")  
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")     

