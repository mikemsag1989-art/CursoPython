"""
a funcao lambda e uma funcao anonima, ou seja, uma funcao que nao e declarada com a palavra-chave def.

"""

# funcao de potencia de um numero
power = lambda x: x ** 2

# funcao que verifica se o numero e par
is_even = lambda x: x % 2 == 0

# funcao que divide um numero por outro
div_num = lambda x, y: x / y

# funcao que inverte uma string
reverse_string = lambda s: s[::-1]  


print(power (5))  # 25
print(power (9)) # 81
print(is_even (4))  # True
print(is_even (7))  # False 
print(div_num (10, 2))  # 5.0
print(div_num (15, 3))  # 5.0
print(reverse_string ("Python"))  # nohtyP
print(reverse_string ("Lambda"))  # adbmaL  


#funcionalidades relacionadas aos filmes:

movies_List = ["Matrix", "Inception", "Interstellar", "The Dark Knight", "Pulp Fiction"]
ratings = {
    "Matrix": [8.7, 9.0, 8.5, 9.2],
    "Inception": [8.8, 8.9, 8.7],
    "Interstellar": [8.6, 8.7, 8.5],
    "The Dark Knight": [9.0, 9.1, 8.9],
    "Pulp Fiction": [8.9, 8.8, 8.7],
    "DGB": [5.0, 4.5, 6.0]
}

# funcao para calcular a media das notas de um filme
average_rating = lambda movie: sum(ratings[movie]) / len(ratings[movie]) if movie in ratings else 0
print(f"Média de notas de Inception: {average_rating('Inception'):.2f}")  # 8.80
print(f"Média de notas de The Dark Knight: {average_rating('The Dark Knight'):.2f}")  # 9.00


# funcao que verifica se um filme esta na lista
is_movie_in_list = lambda movie: movie in movies_List   
print(is_movie_in_list("Matrix"))  # True
print(is_movie_in_list("Avatar"))  # False  

# funcao para recomendar um fulme com base na media das notas
recommend_movie = lambda movie: f"Recomendado: {movie}" if average_rating(movie) >= 8.5 else f"Não recomendado: {movie}"
print(f"Recomendado: {recommend_movie('Pulp Fiction')} a nota é {average_rating('Pulp Fiction'):.2f}")  # Recomendado: Pulp Fiction     
print(f"Recomendado: {recommend_movie('Interstellar')} a nota é {average_rating('Interstellar'):.2f}")  # Recomendado: Interstellar
print(f"Não recomendado: {recommend_movie('DGB')} a nota é {average_rating('DGB'):.2f}")  # Não recomendado: Some Low Rated Movie