moviesList = ["Matrix", "O Poderoso Chefão", "Forrest Gump", "A Procura da Felicidade", "O Iluminado", "Clube da Luta"]

# 1 - interando valores de uma lista com while
index = 0
while index < len(moviesList):
    print(f"Filme: {moviesList[index]}")    
    index += 1  

# 2 - quando a condicao for atendida, interrompe o loop
index = 0
while index < len(moviesList):
    if moviesList[index] == "Forrest Gump":
        print("Filme encontrado! Interrompendo o loop.")
        break
    print(f"Verificando filme: {moviesList[index]}")
    index += 1

# 3 - quando a condicao for atendida, pula para a proxima iteracao
index = 0
while index < len(moviesList):
    if moviesList[index] == "O Iluminado":
        print("Pulando o filme O Iluminado.")
        index += 1
        continue
    print(f"Filme: {moviesList[index]}")
    index += 1    

#4 - avaliacao do filme
movieName = input("Digite o nome do filme para avaliação: \n")  
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))  
total = 0
count = 0   
while count < movieRating:
    rating = float(input(f"Digite a avaliação para o filme {movieName}: \n"))
    total += rating
    count += 1
if movieRating > 0:
    average = total / movieRating       
else:
    average = 0
print(f"Avaliação média do filme {movieName}: {average:.2f}")   


