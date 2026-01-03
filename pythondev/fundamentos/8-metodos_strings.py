movieName = "Top Gun"
movieDescription = """
    Um filme de ação sobre pilotos de caça da Marinha dos EUA.
    Lançado em 1986, estrelado por Tom Cruise.
    Conhecido por suas cenas de voo emocionantes e trilha sonora icônica. """

print (movieName.upper())  #TOP GUN
print (movieName.lower())  #top gun     
print (movieName.title())  #Top Gun
print (movieName.strip())  #Top Gun
print (movieName.replace("Gun", "Pilot"))  #Top Pilot   
print (movieDescription.split(',')) #Separa o texto em uma lista, usando a virgula como separador 
print (movieName.find("Gun"))  #4   retorna a posicao inicial da palavra ou letra
print (movieName.startswith("Top"))  #True
print (movieName.endswith("Gun"))  #True    
print (movieName.center(9, "-"))  #-Top Gun- retorna a string centralizada com 8 caracteres, preenchendo com '-'
print (len(movieName))  #7
