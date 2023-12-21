class TicTacToeGame:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None  # New attribute to store the winner

    def make_move(self, position):
        if self.board[position] == " " and not self.game_over:
            self.board[position] = self.current_player
            self.check_game_over()
            self.switch_player()
            return True
        return False

    def check_game_over(self):
        # Horizontal, vertical, diagonal win conditions
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]             # Diagonal
        ]

        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                self.game_over = True
                self.winner = self.current_player  # Set the winner
                return

        if " " not in self.board:
            self.game_over = True  # Draw condition

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.__init__()

    def display_board(self):
        # Creating a string to represent the board visually
        board_display = ""
        for i in range(3):
            # Extracting each row of the board
            row = self.board[i*3:(i+1)*3]
            # Center align the symbols and join with vertical lines
            board_display += " " + " | ".join(f"{cell:^3}" for cell in row) + " \n"
            # Adding horizontal separators between rows, except for the last row
            if i < 2:
                board_display += "---+---+---\n"
        return board_display

