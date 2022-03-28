board = [["-" for j in range(3)] for i in range(3)]
player1 = "x"
player2 = "o"
players = [player1, player2]


class Game:
    def __init__(self, board):
        self.board = board
        self.jogo_on = True

    def jogar(self, player, posicao):
        lugares = {"a": 0, "b": 1, "c": 2}
        linha = lugares[posicao[0]]
        coluna = int(posicao[1])
        try:
            if self.board[linha][coluna] == "-":
                self.board[linha][coluna] = player
                self.verificar(player)
                if self.jogo_on == True:
                    if player == player1:
                        self.Menu(player2)
                    else:
                        self.Menu(player1)
            else:
                print("Esse lugar já foi escolhido")
                self.Menu(player)
        except Exception:
            print("algo deu errado, tente novamente!")
            self.Menu(player)

    def verificar(self, player):

        if (
            (
                self.board[0][0] == player
                and self.board[0][1] == player
                and self.board[0][2] == player
            )
            or (
                self.board[1][0] == player
                and self.board[1][1] == player
                and self.board[1][2] == player
            )
            or (
                self.board[2][0] == player
                and self.board[2][1] == player
                and self.board[2][2] == player
            )
        ):
            print(f" O jogador {player} foi o vencedor!")
            self.jogo_on = False

        if (
            (
                self.board[0][0] == player
                and self.board[1][0] == player
                and self.board[2][0] == player
            )
            or (
                self.board[0][1] == player
                and self.board[1][1] == player
                and self.board[2][1] == player
            )
            or (
                self.board[0][2] == player
                and self.board[1][2] == player
                and self.board[2][2] == player
            )
        ):
            print(f" O jogador {player} foi o vencedor!")
            self.jogo_on = False

        if (
            self.board[0][0] == player
            and self.board[1][1] == player
            and self.board[2][2] == player
        ) or (
            self.board[2][0] == player
            and self.board[1][1] == player
            and self.board[0][2]
        ):
            print(f" O jogador {player} foi o vencedor!")
            self.jogo_on = False

    def Menu(self, player):
        while self.jogo_on:
            print(self.board)
            posicao = input(f"{player} Qual a posição que você quer ir? ")
            jogo.jogar(player, posicao)
        resp = input("Quer jogar novamente? ")
        if resp[0].lower() == "s":
            self.board = [["-" for j in range(3)] for i in range(3)]
            self.jogo_on = True
            self.Menu(player1)


jogo = Game(board)
jogo.Menu(player1)
