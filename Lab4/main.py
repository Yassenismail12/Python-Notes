import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError("Subclasses must implement make_move")

class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                pos = int(input(f"{self.name}, enter position (1-9): ")) - 1
                if board.is_valid_move(pos):
                    board.update(pos, self.symbol)
                    break
                else:
                    print("Invalid position. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

class ComputerPlayer(Player):
    def make_move(self, board):
        available = [pos for pos in range(9) if board.is_valid_move(pos)]
        pos = random.choice(available)
        board.update(pos, self.symbol)
        print(f"{self.name} chooses position {pos + 1}")

class Board:
    def __init__(self):
        self._grid = [[' ' for _ in range(3)] for _ in range(3)]

    def __str__(self):
        s = "   1 2 3\n"
        for i in range(3):
            s += f"{i+1} "
            for j in range(3):
                s += f"{self._grid[i][j]} "
            s += "\n"
        return s

    def display(self):
        print(self)

    def update(self, pos, symbol):
        i, j = divmod(pos, 3)
        self._grid[i][j] = symbol

    def is_valid_move(self, pos):
        if not (0 <= pos < 9):
            return False
        i, j = divmod(pos, 3)
        return self._grid[i][j] == ' '

    def check_winner(self):
        for row in self._grid:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        for j in range(3):
            if self._grid[0][j] == self._grid[1][j] == self._grid[2][j] != ' ':
                return self._grid[0][j]
        if self._grid[0][0] == self._grid[1][1] == self._grid[2][2] != ' ':
            return self._grid[0][0]
        if self._grid[0][2] == self._grid[1][1] == self._grid[2][0] != ' ':
            return self._grid[0][2]
        return None

    def is_full(self):
        return all(cell != ' ' for row in self._grid for cell in row)

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = player1

    def switch_turns(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self):
        print("Tic-Tac-Toe Game!\n")
        while True:
            self.board.display()
            self.current_player.make_move(self.board)
            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f"{self.current_player.name} ({winner}) wins!")
                break
            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break
            self.switch_turns()

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe")
    choice = input("Do you want to play with a friend (1) or vs computer (2)? ")
    if choice == '1':
        name1 = input("Player 1 name: ")
        name2 = input("Player 2 name: ")
        player1 = HumanPlayer(name1, 'X')
        player2 = HumanPlayer(name2, 'O')
    elif choice == '2':
        name = input("Your name: ")
        player1 = HumanPlayer(name, 'X')
        player2 = ComputerPlayer("Computer", 'O')
    else:
        print("Invalid choice. Exiting.")
        exit()
    game = Game(player1, player2)
    game.play()
