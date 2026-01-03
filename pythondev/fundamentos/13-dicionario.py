filmInception = { # criando um dicionário - listas são criadas com colchetes [] e dicionários com chaves {}
    "title": "Inception",   
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": ["Sci-Fi", "Action", "Thriller"],
    "rating": 8.8
                }
print(filmInception)

print(len(filmInception))
print(type(filmInception))

# 1 - recuperar um elemento do dicionário
print(filmInception["director"])
print(filmInception.get("year"))

# 2  - buscar apenas as chaves do dicionário
print(filmInception.keys())

# 3 - buscar apenas os valores do dicionário
print(filmInception.values())

# 4 - buscar itens do dicionário com chave e valor
print(filmInception.items())    

# 5 - adicionar um novo par chave/valor ao dicionário
filmInception["budget"] = 160000000 # adicionando o orçamento do filme
print(filmInception)

# 6 - modificar um valor existente no dicionário
filmInception["rating"] = 9.0 # atualizando a avaliação do filme        
print(filmInception)

# 7 - remover um par chave/valor do dicionário
del filmInception["budget"] # removendo o orçamento do filme
filmInception.pop("genre") # removendo o gênero do filme
print(filmInception)

