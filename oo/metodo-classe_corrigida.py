class Game:
    total_games = 0
    games = []  # lista para armazenar todos os jogos criados

    def __init__(self, name="", yearLaunch=0, multiplayer=False, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        self.totalEvaluation = 0
        self.evaluators = 0

        Game.total_games += 1
        Game.games.append(self)

    def __str__(self):
        return f"Game: {self.name}"

    def technical_sheet(self):
        print("### Dados do Jogo ###")
        print(f"Nome: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Nota inicial: {self.note}\n")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        if self.evaluators == 0:
            return 0
        return self.totalEvaluation / self.evaluators

    @classmethod
    def print_total_games_stats(cls):
        print("#### Estatísticas Gerais ####")
        print(f"Total de jogos criados: {cls.total_games}")

        total_notes = 0
        total_evaluators = 0

        for game in cls.games:
            total_notes += game.totalEvaluation
            total_evaluators += game.evaluators

        if total_evaluators > 0:
            print(f"Média geral dos jogos: {total_notes / total_evaluators:.2f}")
        else:
            print("Nenhuma avaliação registrada.")

                

game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)

game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)

game1.technical_sheet()
game2.technical_sheet() 

print (f"A média do jogo {game1.name} é: {game1.average()} \n")
print (f"A média do jogo {game2.name} é: {game2.average()} \n")

Game.print_total_games_stats()  # estatísticas gerais            