filmList =["Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction"]

#1 - tamanho da lista
print (len(filmList))   

#2 - Recupera o indice de um item da lista
print (filmList.index("The Dark Knight"))   

#3 - Adicionar um item na lista
filmList.append("Forrest Gump") 
print (filmList)

#4 - Ordenar a lista
filmList.sort()
print (filmList)    

#5- Copiar os itens de uma lista para outra
newFilmList = filmList.copy()   
newFilmList.remove("Pulp Fiction")
print (newFilmList)

#6 - Remove todos os itens da lista
newFilmList.clear()   
print (newFilmList) 

