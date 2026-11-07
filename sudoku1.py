
import sys
from clingo.application import Application, clingo_main


class ClingoApp(Application):
    def main(self, control, files):
        # Load the Sudoku puzzle
        for file in files:
            control.load(file)

        # Rules for solving Sudoku
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

        control.ground([("base", [])])
        control.solve()

    def print_model(self, model, printer):
        atoms = sorted(
            str(atom) for atom in model.symbols(shown=True)
        )
        print(" ".join(atoms))


if __name__ == "__main__":
    sys.exit(clingo_main(ClingoApp(), sys.argv[1:]))
