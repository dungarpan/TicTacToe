class TicTacToe:
    def __init__(self) -> None:
        print("New game instance")
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.p1 = "X"
        self.p2 = "O"
        self.turns =0
        self.pos = "00"

    def isWon(self) -> bool:
        for i in self.board:
            if i[0] != "-" and i[0]==i[1]==i[2]:
                return True
        for i in range(3):
            if self.board[i][0] !="-" and self.board[i][0]==self.board[i][1]==self.board[i][2]:
                return True
        if self.board[0][0]!="-" and self.board[0][0]==self.board[1][1]==self.board[2][2]:
            return True
        if self.board[0][2]!="-" and self.board[0][2]==self.board[1][1]==self.board[2][0]:
            return True
        return False
    
    def insertToken(self, player):
        x,y = int(self.pos[0]), int(self.pos[1])
        print(x,y)
        if player==1:
            self.board[x][y] = self.p1
        else:
            self.board[x][y] = self.p2
        print(self.board)
        
    def start(self):
        while not self.isWon() and self.turns<9:
            if self.turns%2==0:
                self.pos = input("Player 1's turn. select your spot e.g [00,12,21,12]")
                self.insertToken(1)
            else:
                self.pos = input("Player 2's turn. select your spot e.g [00,12,21,12]")
                self.insertToken(2)
            self.turns+=1
            self.display()
        
        if self.turns==9:
            print("The game has been drawed")
        if self.turns%2==1:
            print("Player 1 has won the game. Good work!")
        else:
            print("Player 2 has won the game. Good work!")

    def display(self):
         print(" ".join(self.board[0]) + "\n" + " ".join(self.board[1]) + "\n" + " ".join(self.board[2]) + "\n")
    def __str__(self) -> str:
        return " ".join(self.board[0]) + "\n" + " ".join(self.board[1]) + "\n" + " ".join(self.board[2]) + "\n"
    
def main():
    game = TicTacToe()
    game.display()
    game.start()

main()