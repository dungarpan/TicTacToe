class TicTacToe:
    def __init__(self) -> None:
        print("New game instance")
        self.board = [["-","-","-"] for i in range(3)]
        self.p1 = "X"
        self.p2 = "O"

    def isWon(self) -> bool:
        for i in self.board:
            if not (i[0] != "-" and i[0]==i[1] and i[1]==i[2]):
                return False
        for i in range(3):
            if not(i[i][0] !="-" and self.board[i][0]==self.board[i][1] and self.board[i][1]==self.board[i][2]):
                return False
        if not (self.board[0][0]!="-" and self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]):
            return False
        if not (self.board[0][2]!="-" and self.board[0][2]==self.board[1][1] and self.board[1][1]==self.board[2][0]):
            return False
        return True

    def start(self):
        while not self.isWon():
            pass


    def display(self):
         print(" ".join(self.board[0]) + "\n" + " ".join(self.board[1]) + "\n" + " ".join(self.board[2]) + "\n")
    def __str__(self) -> str:
        return " ".join(self.board[0]) + "\n" + " ".join(self.board[1]) + "\n" + " ".join(self.board[2]) + "\n"
    
def main():
    game = TicTacToe()
    game.display()
    print(game)

main()