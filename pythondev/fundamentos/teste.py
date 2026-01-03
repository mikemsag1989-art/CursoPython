num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

operacao = input ("Digite a operacao desejada: + - * ou /\n")           

# realizar a operacao de acordo com a escolha do usuario 
if operacao == "+":
    resultado = num1 + num2 
elif operacao == "-":
    resultado = num1 - num2     
elif operacao == "*":
    resultado = num1 * num2     
elif operacao == "/":
    resultado = num1 / num2 
else:       
    print ("Operação inválida")
    exit()  

print (f"O resultado da operacão é: {resultado}")
