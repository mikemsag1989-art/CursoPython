# 1 - Listando valores de 0 a 10 que sejam menores do que 4
listNumbers = [number for number in range(10) if number < 4]
print(listNumbers)  

# lista de filmes
moviesList = ["Matrix", "O Poderoso Chefão", "Forrest Gump", "A Procura da Felicidade", "O Iluminado", "Clube da Luta"]

# 2 - Filmes que possuem a letra "e" no nome
moviesWithE = [movie for movie in moviesList if "e" in movie]
print(moviesWithE)  

# 3 - Filmes que assisti
watchedMovies = [movie for movie in moviesList if movie != "O Iluminado"]
print(watchedMovies)

# 4 - encontrando um filme pelo nome    
while True:
    searchName = input("Digite o nome do filme para busca: \n")  
    if searchName.lower() == "sair":
        print("Encerrando a busca de filmes.")
        break
    foundMovies = [movie for movie in moviesList if  searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme encontrado: {foundMovies[0]}")
        break
    else:
        print("Filme não encontrado. Tente novamente.")

