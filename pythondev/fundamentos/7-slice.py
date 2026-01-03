movieName = "Top Gun"

#string [inicio:fim] - indice comeca na posicao 0 | indice final -1

#1 - Busca toda String a partir  da primera posicao
print (movieName[0:])  #Top Gun

#2 - Busca toda String até a ultima posicao
print (movieName[:7])  #Top Gun

#3 - Busca toda String da terceira posicao ate a ultima posicao
print (movieName[2:])  #p Gun

"""
string [inicio:fim:passo]
indice comeca na posicao 0 | indice final -1
passo - determina o incremento. Por padrao esse numero é o 1.
"""

#4 - Busca toda a string de 2 em 2 caracteres
print (movieName[0::2])  #TpGu

#5 - Busca toda a string nos indices impares
print (movieName[1::2])  #o n

#6 - Inverte uma string de tras para frente
print (movieName[::-1])  #nuG poT

