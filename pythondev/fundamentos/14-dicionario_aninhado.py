import pprint



filmDict = { # criando um dicionário aninhado - listas são criadas com colchetes [] e dicionários com chaves {}
        "Inception": {
          "director": "Christopher Nolan",
          "year": 2010,
          "genre": ["Sci-Fi", "Action", "Thriller"],
          "rating": 8.8
                    },
        "Interstellar": {
          "director": "Steben Spielberg",
          "year": 2014,
          "genre": ["Sci-Fi", "Action"],
          "rating": 7
        },
        "The Dark Knight": {
          "director": "Christopher Nolan",
          "year": 2008,
          "genre": ["Action", "Crime", "Drama"],
          "rating": 9.0
        }
    }
pp = pprint.PrettyPrinter(depth=4) # definindo a profundidade de exibição do dicionário aninhado
pp.pprint(filmDict)

# 1 - Busca uma informação específica dentro do dicionário aninhado
print(filmDict["Inception"]["director"]) # recuperando o diretor do filme Inception
print(filmDict["Interstellar"]["year"]) # recuperando o ano do filme Interstellar

# 2 - Adicionando um novo filme ao dicionário aninhado
filmDict["Avatar"] = {
          "director": "James Cameron",
          "year": 2009,
          "genre": ["Action", "Adventure", "Fantasy"],
          "rating": 7.8
        }

pp.pprint(filmDict)

# 3 - adicionando um gênero ao filme The Dark Knight
filmDict["The Dark Knight"]["genre"].append("Thriller") # adicionando o gênero Thriller ao filme The Dark Knight
pp.pprint(filmDict)

# 4 - removendo um filme do dicionário aninhado
del filmDict["Interstellar"] # removendo o filme Interstellar do dicionário aninhado
pp.pprint(filmDict) 

