from tic_tac_toe import TicTacToeGame

# Global dictionary to store active Tic Tac Toe games
active_games = {}


def start_tic_tac_toe(channel_id):
    if channel_id in active_games:
        return "A Tic Tac Toe game is already in progress in this channel."

    game = TicTacToeGame()
    active_games[channel_id] = game
    return "Tic Tac Toe game started! Player X goes first.(Choose a number 0-8)"


def make_move(channel_id, position, player_id):
    if channel_id not in active_games:
        return "No active Tic Tac Toe game in this channel. Start a new game with `start tictactoe`."

    game = active_games[channel_id]

    if not game.make_move(position):
        return f"Invalid move. It's still Player {game.current_player}'s turn."

    if game.game_over:
        if game.winner:
            response = f"Game over! Player {game.winner} wins!"
        else:
            response = "Game over! It's a draw!"
        del active_games[channel_id]
        return response
    return f"Player {game.current_player}, it's your turn:\n{game.display_board()}"


def end_tic_tac_toe(channel_id):
    if channel_id not in active_games:
        return "No active Tic Tac Toe game to end."

    del active_games[channel_id]
    return "Tic Tac Toe game ended."


def handle_response(message, author_id):
    args = message.split()
    command = args[0]
    print(command)
    if command == 'start tictactoe':
        return start_tic_tac_toe(author_id)
    elif command == 'move':
        if len(args) < 2:
            return "Please specify a position to move."
        try:
            position = int(args[1])
        except ValueError:
            return "Invalid position. Please specify a number between 0 and 8."
        return make_move(author_id, position, author_id)
    elif command == 'end tictactoe':
        return end_tic_tac_toe(author_id)
    else:
        return "Unknown command."
