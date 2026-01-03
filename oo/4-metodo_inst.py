class Game: # Definição da classe Game, com construtor e método __str__, mas sem métodos adicionais
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name  
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        self.totalEvaluation = 0
        self.evaluators = 0
        
    def __str__(self): # Método para representar o objeto como string, usado na função print()
        return f"Game: {self.name}"
    
    def technical_sheet(self): # Método para exibir a ficha técnica do jogo
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer?: {self.multiplayer}")
        print(f"Avaliação do Jogo: {self.note}\n")
        
    def evaluate(self, note): # Método para avaliar o jogo com uma nota 
        self.totalEvaluation += note
        self.evaluators += 1
        
    def average(self):
        print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")
    
game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)
game1.average()
game2.average()
