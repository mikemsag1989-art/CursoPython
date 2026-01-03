# 1 - funcao para imprimir um nome completo
def print_full_name(first_name, last_name):
    print(f"Nome completo: {first_name} {last_name}")

print_full_name("João", "Silva")

# 2 - funcao para somar dois numeros
def sum_two_numbers(num1, num2):
    return num1 + num2  

print(f"Soma: {sum_two_numbers(5, 10)}")

# 3 - funcao com parametro default
def adress(coutry="Brasil"):
    print(f"País: {coutry}")

adress()
adress("Portugal")

# 4 - funcao para avaliar um filme
def rate_movie(movie_name, number_of_ratings):
    total = 0
    for i in range(number_of_ratings):
        rating = float(input(f"Digite a avaliação {i + 1} para o filme {movie_name}: \n"))
        total += rating
    if number_of_ratings > 0:
        average = total / number_of_ratings   
    else:
        average = 0

    print (f"A média de nota do filme {movie_name} é: {average:.2f}")

rate_movie("Matrix", 3)


