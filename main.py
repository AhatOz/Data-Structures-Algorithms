from View import View
from SudokuFourModel import SudokuFourModel
import sys


class Controller:

    @staticmethod
    def main(args):
        Controller().run(args)

    def __init__(self):
        self.__model = SudokuFourModel()
        self.__view = View()

    def run(self, args):
        if len(args) == 2:
            try:
                self.__model.load_from_file(args[1])
                self.__view.show_board(self.__model.board, self.__model.locked)
                self.__model.recursive_solve()
                self.__view.show_board(self.__model.board, self.__model.locked)
                self.__view.show_steps(self.__model.steps)
            except Exception as e:
                self.__view.show_error(e)
        else:
            self.__view.show_error("No file provided")


if __name__ == "__main__":
    Controller.main(sys.argv)
