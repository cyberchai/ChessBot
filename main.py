import random
import datetime
import chess
import chess.engine 
# pip3 install python-chess

"""
Chaira and Glory

FINAL PROJECT IMPLEMENTATION

"""

"""
Initial function that is called to start the game and prompt the user to choose to play as Black or White.
"""
def init_set():
    print('=====================================================\n\t\t\tCSC 290 Minimax Chess Bot V.02 by Chaira and Glory\t\t\t\n=====================================================')
    print('Time:', datetime.datetime.now())
    comp = ''
    while(comp not in ['w', 'b', 'white', 'black', 'wh', 'bl']):
        comp = input('Computer Player? (w=white/b=black): ')
    # starting_pos = input('Starting FEN position? (hit ENTER for standard starting position): ')
    if 'b' in comp:
        print('You are playing as BLACK. The computer will start first.\n')
    elif 'w' in comp:
        print('You are playing as WHITE. Please begin the first move.\n')
    print('\n')
    return comp

"""
Updates the chess board
"""
def update_board(board):
    print(board)

"""
A4: Uses the minimax function to decide the most optimal next move.
We can play around with the depth tuning parameter to balance efficiency with quality.

A3:Generates a list of legal chess moves based on the current board, and selects one at random using the chess engine library.
"""

def get_computer_move(board, depth=2):
    _, best_move = minimax(board, depth, float('-inf'), float('inf'), True)
    # validate the move:
    if best_move in board.legal_moves:
        return best_move
    else:
        print("Minimax returned an illegal move...")
        print(best_move)
        print(f"Current board:\n\n{board}")
        print(f"Legal moves: {[move.uci() for move in board.legal_moves]}") # for debugging
        return random.choice(list(board.legal_moves)) # Random if minimax fails
    
"""
Makes a move based on the current board and turn.
"""
def move(comp, board, turn):
    if turn == 0:
        move_choice = get_computer_move(board)
        if move_choice:
            board.push(move_choice)
            print(f"Computer moved: {move_choice}")
    else:
        move_choice = None
        while move_choice not in board.legal_moves:
            user_input = input('Enter your move (eg. e2e4): ')
            try:
                move_choice = chess.Move.from_uci(user_input)
            except:
                print("Invalid format, please use standard notation like e2e4")
            if move_choice not in board.legal_moves:
                print("Sorry, you can't make that move. Please enter a different move.")
        board.push(move_choice)
        print(f"You moved: {move_choice}")

"""
Evaluates the given board score. WHITE corresponds to a positive number, BLACK corresponds to a negative number. 0 corresponds to a draw/equivalence.https://www.chess.com/terms/chess-piece-valuehttps://www.chess.com/terms/chess-piece-valuehttps://www.chess.com/terms/chess-piece-value
We are basing the piece values off of the provided: https://www.chess.com/terms/chess-piece-value
"""
def evaluate_board(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0 # Just to account for all pieces, he is assigned a 0 (invaluable -- he is the game)
    }

    score = 0
    for piece in piece_values:
        score += len(board.pieces(piece, chess.WHITE)) * piece_values[piece]
        score -= len(board.pieces(piece, chess.BLACK)) * piece_values[piece]

    return score



"""
Minimax algorithm with alpha and beta used for pruning to save time.
"""
def minimax(board, depth, alpha, beta, maxPlayer):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None  # tupple
    
    bestMove = None

    if maxPlayer:
        maxEval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, childBestMove = minimax(board, depth-1, alpha, beta, False) # we don't actually need to use childBestMove though, so we could just do eval, _ = ... or eval = ...[0]. But for clarity's sake so I don't forget, here.
            board.pop()

            if eval > maxEval:
                maxEval = eval
                bestMove = move

            alpha = max(alpha, eval)

            if beta <= alpha:
                break
        return maxEval, bestMove
    
    else:
        minEval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, childBestMove = minimax(board, depth-1, alpha, beta, True)
            board.pop()
            
            if eval < minEval:
                minEval = eval
                bestMove = move

            # minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval, bestMove


"""
Main method for this chess program.
"""
def main():
    comp = init_set()
    board = chess.Board()

    update_board(board) # initial board

    checkmate = False

    # turn tracker:
    if 'b' in comp:
        i=0
    else:
        i=1

    # while(not checkmate):
    while(not board.is_game_over()):
        turn = i%2
        move(comp, board, turn)
        update_board(board)

        if board.is_checkmate():
            print("Checkmate")
            break
        elif board.is_stalemate():
            print("Stalemate (tie)")
            break

        i+=1

if __name__ == '__main__':
    main()