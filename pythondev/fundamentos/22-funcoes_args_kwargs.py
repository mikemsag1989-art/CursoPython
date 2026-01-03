import pprint
from textwrap import indent

"""
*args - Utilizamos quando não sabemos quantos argumentos serão passados em uma função. Os argumentos são recebidos como uma tupla.

"""

def sum(*num):
    total = 0
    for n in num:
        total += n
    print(f"A soma é: {total}") 

sum(1, 2, 3, 4, 5)
sum(10, 20, 30) 
    


"""
**kwargs - Utilizamos quando não sabemos quantos argumentos nomeados serão passados em uma função (chave e valor). Os argumentos são recebidos como 
           um dicionário.

"""

#pp = pprint.PrettyPrinter(depth=4)

# 2 - Apresentacao de cursos
def presentation(**course):
    for key, value in course.items():
        print(f"{key}: {value}")
print("Lista de cursos: \n")        
presentation(cursoName="Python Básico", nivel="Python Intermediário", categoria="Programação")
presentation(cursoName="Java Básico", nivel="Java Intermediário", categoria="Programação", cargaHoraria=40)
presentation(cursoName="JavaScript Básico", nivel="JavaScript Avançado", categoria="Programação", plataforma="Udemy", preco=29.90)
