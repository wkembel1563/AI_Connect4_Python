from game import *
from utils import verify, load_board
import sys

MODE = 0

if __name__ == "__main__":


    # verify command line input
    #utils.verify(sys.argv)

    # initialize game
    _, mode, board_file, whos_next, depth = sys.argv
    
    init_board_state, next_player_color = utils.load_board(board_file)

    game = ConnectFour(mode, init_board_state, next_player_color, whos_next, depth)

    # begin
    game.play()
