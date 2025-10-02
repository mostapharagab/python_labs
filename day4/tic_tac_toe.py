import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def make_move(self, board):
        raise NotImplementedError("Subclasses must implement make_move method")

class HumanPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
    
    def make_move(self, board):
        while True:
            try:
                print(f"\n{self.name}'s turn ({self.symbol})")
                position = int(input("Enter position (1-9): "))
                
                if position < 1 or position > 9:
                    print("Invalid position! Please enter a number between 1-9.")
                    continue
                
                row = (position - 1) // 3
                col = (position - 1) % 3
                
                if board.update(row, col, self.symbol):
                    return True
                else:
                    print("Position already taken! Choose another position.")
                    
            except ValueError:
                print("Invalid input! Please enter a number between 1-9.")

class ComputerPlayer(Player):
    def __init__(self, name="Computer", symbol="O"):
        super().__init__(name, symbol)
    
    def make_move(self, board):
        print(f"\n{self.name}'s turn ({self.symbol})")
        available_positions = []
        for i in range(3):
            for j in range(3):
                if board._grid[i][j] == ' ':
                    available_positions.append((i, j))
        
        if available_positions:
            row, col = random.choice(available_positions)
            board.update(row, col, self.symbol)
            print(f"Computer chooses position {row * 3 + col + 1}")
            return True
        
        return False

class Board:
    def __init__(self):
        self._grid = [[' ' for _ in range(3)] for _ in range(3)]
    
    def display(self):
        print("\nCurrent Board:")
        print("Positions:     Current State:")
        
        for i in range(3):
            pos_row = f" {i*3+1} | {i*3+2} | {i*3+3} "
            state_row = f" {self._grid[i][0]} | {self._grid[i][1]} | {self._grid[i][2]} "
            print(f"{pos_row}     {state_row}")
            
            if i < 2:
                print("-----------     -----------")
    
    def __str__(self):
        result = ""
        for i in range(3):
            result += f" {self._grid[i][0]} | {self._grid[i][1]} | {self._grid[i][2]} \n"
            if i < 2:
                result += "-----------\n"
        return result
    
    def update(self, row, col, symbol):
        if 0 <= row < 3 and 0 <= col < 3 and self._grid[row][col] == ' ':
            self._grid[row][col] = symbol
            return True
        return False
    
    def check_winner(self):
        for row in self._grid:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        for col in range(3):
            if self._grid[0][col] == self._grid[1][col] == self._grid[2][col] != ' ':
                return self._grid[0][col]
        
        if self._grid[0][0] == self._grid[1][1] == self._grid[2][2] != ' ':
            return self._grid[0][0]
        
        if self._grid[0][2] == self._grid[1][1] == self._grid[2][0] != ' ':
            return self._grid[0][2]
        
        return None
    
    def is_full(self):
        for row in self._grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_turn = 0
    
    def setup_players(self):
        print("=" * 50)
        print("         Welcome to Tic-Tac-Toe!")
        print("=" * 50)
        
        while True:
            try:
                mode = int(input("\nDo you want to play with a friend (1) or vs computer (2)? "))
                
                if mode == 1:
                    print("\n--- Two Player Mode ---")
                    player1_name = input("Enter Player 1 name: ")
                    player2_name = input("Enter Player 2 name: ")
                    
                    self.players.append(HumanPlayer(player1_name, 'X'))
                    self.players.append(HumanPlayer(player2_name, 'O'))
                    
                    print(f"\n{player1_name} will play as 'X'")
                    print(f"{player2_name} will play as 'O'")
                    break
                    
                elif mode == 2:
                    print("\n--- Player vs Computer Mode ---")
                    player_name = input("Enter your name: ")
                    
                    self.players.append(HumanPlayer(player_name, 'X'))
                    self.players.append(ComputerPlayer("Computer", 'O'))
                    
                    print(f"\n{player_name} will play as 'X'")
                    print("Computer will play as 'O'")
                    break
                    
                else:
                    print("Invalid option! Please enter 1 or 2.")
                    
            except ValueError:
                print("Invalid input! Please enter 1 or 2.")
    
    def switch_turns(self):
        self.current_turn = (self.current_turn + 1) % 2
    
    def play(self):
        self.setup_players()
        
        print(f"\n{self.players[0].name} goes first!")
        
        while True:
            self.board.display()
            
            current_player = self.players[self.current_turn]
            current_player.make_move(self.board)
            
            winner_symbol = self.board.check_winner()
            if winner_symbol:
                self.board.display()
                winner = next(player for player in self.players if player.symbol == winner_symbol)
                print(f"\n🎉 Congratulations! {winner.name} wins! 🎉")
                break
            
            if self.board.is_full():
                self.board.display()
                print("\n🤝 It's a draw! 🤝")
                break
            
            self.switch_turns()
        
        print("\nThanks for playing Tic-Tac-Toe!")

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()

