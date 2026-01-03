# 1
palavra = (input("Digite uma palavra: \n"))
n = int (input("Digite o número de vezes para imprimir a mesma palavra: \n"))

palavraEspaco = palavra + " "

resultado = palavraEspaco * n

print (f"A palavra {palavra} será repetida {n} vezes: {resultado}\n")


# 2
texto = "Python é muito interessante"
palavras = texto.split() # separa o texto em palavras
textoInvertido = " ".join(palavras[::-1]) # junta as palavras na ordem inversa
print (textoInvertido) # resultado "interessante muito é Python"