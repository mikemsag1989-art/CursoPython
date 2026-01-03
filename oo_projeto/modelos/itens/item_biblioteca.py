from abc import ABC, abstractmethod # importa ABC e abstractmethod para criar classes abstratas e metodos abstratos

class ItemBiblioteca(ABC): # ABC = Abstract Base Class, classe abstrata que nao pode ser instanciada diretamente, apenas herdada
    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
    
    @abstractmethod # decorator que torna o metodo abstrato, obrigando as subclasses a implementarem esse metodo
    def aplicar_desconto(self):
        pass # pass indica que o metodo nao tem implementacao na classe abstrata, apenas na subclasse