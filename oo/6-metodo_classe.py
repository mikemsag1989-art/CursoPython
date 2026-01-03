class Game:
    total_games = 0 # Variável de classe para contar o número total de jogos
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name  
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1 # Variável de classe, Incrementa o contador de jogos ao criar uma nova instância, 
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
        
    def average(self): # Método para calcular a média das avaliações do jogo
        print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")
        
    @classmethod # Método de classe para exibir estatísticas gerais dos jogos, usando a variável de classe
    def print_total_games_stats(cls): # cls é uma convenção para o primeiro parâmetro de métodos de classe, referenciando a própria classe
        print("####Estatísticas Gerais dos Jogos####")
        print(f"Total de jogos criados: {cls.total_games}")
        print(f"Média geral de avaliações por jogo: {cls.total_games and sum(game.totalEvaluation for game in cls.__subclasses__()) / cls.total_games or 0}")
        
game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("Red Dead Redemption 2", 2018, False, 10.0)

game1.technical_sheet()
game2.technical_sheet()
game3.technical_sheet()
game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)

Game.print_total_games_stats() # Chamando o método de classe para exibir as estatísticas gerais dos jogos