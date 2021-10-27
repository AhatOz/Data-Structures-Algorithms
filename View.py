class View:

    def __init__(self):
        pass

    def show_board(self, board, locked):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if locked[i][j]:
                    print("[{}]".format(board[i][j]), end="")
                else:
                    if board[i][j] == 0:
                        print(" _ ", end="")
                    else:
                        print(" {} ".format(board[i][j]), end="")
            print("")

    def show_steps(self, steps):
        print("The solution took {} steps.".format(steps))

    def show_error(self, error):
        print("Error: {}".format(error))
