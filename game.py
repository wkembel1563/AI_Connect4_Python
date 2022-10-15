
    game = ConnectFour(mode, init_board_state, whos_next, depth)

class ConnectFour:
    def __init__(self, mode, board, next_color, next_player, depth):
        self.mode = mode
        self.board = board
        self.next_player = next_player
        self.depth = depth

    def play():
        if self.mode == "interactive":
            self.play_interactive()

        elif self.mode == "one-move":
            self.play_one_move()

        else:
            print("Play Error: Invalid play mode")
            exit(1)

    def play_interactive():

        # figure out who is red/green
        # next_color shows which color plays next (defined in input file)
        # next_player shows who plays next (computer or human)

        # enter game loop

        # COMPUTER
            # print game state for computer, exit if full

            # let computer move

            # save board to computer.txt

            # print game state after computer's move, exit if full

        # HUMAN
            # prompt user for valid move (loop)
            
            # make move

            # save board to human.txt

        pass
    
    def play_one_move():
        pass

    def minimax():
        # store moves as tuples which can index specific positions in numpy board
        pass
