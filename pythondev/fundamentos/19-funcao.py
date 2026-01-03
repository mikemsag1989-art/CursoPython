 # 1 - funcao para imprimir uma mensagem
def welcome():
    print("Bem-vindo ao sistema de avaliação de filmes!")

# for i in range(10):
#     welcome()    


# 2 - funcao para calcular a média de notas
def calculate_average():
    numberOfRatings = int(input("Digite quantas avaliações deseja fazer: \n"))
    total = 0
    for i in range(numberOfRatings):
        rating = float(input(f"Digite a avaliação {i + 1}: \n"))
        total += rating
    if numberOfRatings > 0:
        average = total / numberOfRatings   
        #print(f"A média das avaliações é: {average}")   
    else:
        average = 0
        
    return average # cuidado com indentação, o return deve estar no mesmo nível do if


print(f"A média das avaliações é: {calculate_average():.2f}")

# 3 - funcao para cadastrar um filme
def create_movie():
    movieName = input("Digite o nome do filme que deseja cadastrar: \n")
    year = int(input("Digite o ano do filme: \n"))
    preco = float(input("Digite o preço do filme: \n"))
    print(f"O filme {movieName.upper()} lançado em {year} custa R$ {preco:.2f} e foi cadastrado com sucesso!")
    
create_movie()











