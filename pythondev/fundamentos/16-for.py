moviesList = ["Matrix", "O Poderoso Chefão", "Forrest Gump", "A Procura da Felicidade", "O Iluminado", "Clube da Luta"]

# 1 - interando valores de uma lista
for movie in moviesList:
    print(f"Filme: {movie}")    

# 2 - quando a condicao for atendida, interrompe o loop
for movie in moviesList:
    if movie == "Forrest Gump":
        print("Filme encontrado! Interrompendo o loop.")
        break
    print(f"Verificando filme: {movie}")

# 3 - quando a condicao for atendida, pula para a proxima iteracao
for movie in moviesList:
    if movie == "O Iluminado":
        print("Pulando o filme O Iluminado.")
        continue
    print(f"Filme: {movie}")


#4 - avaliacao do filme
movieName = input("Digite o nome do filme para avaliação: \n")  
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
for i in range(movieRating):
    rating = float(input(f"Digite a avaliação para o filme {movieName}: \n"))
    total += rating

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Avaliação média do filme {movieName}: {average:.2f}")

