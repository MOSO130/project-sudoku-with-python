import clingo
import sys
from sudoku_board import Sudoku
from clingo.application import Application, clingo_main



class Context:
    def __init__(self, board: Sudoku):
        self.board = board

    def initial(self) -> list[clingo.Symbol]:
        symbols = []

        for (row, col), value in sorted(self.board.sudoku.items()):
            symbols.append(
                clingo.Function(
                    "",
                    [
                        clingo.Number(row),
                        clingo.Number(col),
                        clingo.Number(value)
                    ]
                )
            )

        return symbols

class ClingoApp(Application):
   
    def main(self, control, files):
        with open(files[0], "r") as file:
            board = Sudoku.from_str(file.read())

        context = Context(board)

        control.load("sudoku_py.lp")

        control.add("base", [], """
            row(1..9).
            col(1..9).
            num(1..9).

            1 { sudoku(R,C,N) : num(N) } 1 :-
                row(R), col(C).

            :- initial(R,C,N), not sudoku(R,C,N).

            :- sudoku(R,C1,N), sudoku(R,C2,N),
               C1 != C2.

            :- sudoku(R1,C,N), sudoku(R2,C,N),
               R1 != R2.

            :- sudoku(R1,C1,N), sudoku(R2,C2,N),
               (R1-1)/3 = (R2-1)/3,
               (C1-1)/3 = (C2-1)/3,
               R1 != R2.

            :- sudoku(R1,C1,N), sudoku(R2,C2,N),
               (R1-1)/3 = (R2-1)/3,
               (C1-1)/3 = (C2-1)/3,
               C1 != C2.

            #show sudoku/3.
        """)

        control.ground([("base", [])], context=context)
        control.solve()

    
   
    
    
   

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)






if __name__ == "__main__":
    clingo_main(ClingoApp(), sys.argv[1:])
