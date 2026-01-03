filmSet = {"Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction"}
print (type(filmSet))

# 1 - Busca o tamanho do set
print (len(filmSet))    

# 2 - True e 1 sao considerados iguais em um set
exampleSet = {"Inception", True, 1, 8.7} # true e 1 sao considerados iguais logo o set tera apenas 3 elementos
print (exampleSet)  

#3 - adiciona um item no set
filmSet.add("Forrest Gump") 
print (filmSet)

#4 - Remove um item do set
exampleSet.remove(True)
exampleSet.remove(8.7)
print (exampleSet)


