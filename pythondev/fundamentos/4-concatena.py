# Utilizando o Input
name = input ("Digite o nome do filme: \n")
yearLauch = int (input ("Digite o ano de lançamento: \n"))
noteMovie = float (input ("Digite a nota do filme: \n"))

print ("Dados do Filme:")
print ("================================")

# #alternativa 1
# print ("Nome do Filme:", name)
# print ("Ano de Lançamento:", yearLauch)
# print ("Nota do Filme:", noteMovie) 

# #alternativa 2 - concatenação
# print ("Nome do Filme:", name, "\nAno de Lançamento:", yearLauch, "\nNota do Filme:", noteMovie)


# #alternativa 3 - f string (formatted string)
print (f"Nome do Filme: {name}\n"
       f"Ano de lançamento: {yearLauch}\n"
       f"Nota do Filme: {noteMovie}")    

