from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

  
    def __str__(self) -> str:
        lines = []

        for row in range(1, 10):
            groups = []

            for start_col in (1, 4, 7):
                numbers = []

                for col in range(start_col, start_col + 3):
                    value = self.sudoku.get((row, col), "-")
                    numbers.append(str(value))

                groups.append(" ".join(numbers))

            lines.append("  ".join(groups))

            
            if row in (3, 6):
                lines.append("")


        return "\n".join(lines)


    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        
        for atom in model.symbols(shown=True):
            if atom.name == "sudoku" and len(atom.arguments) == 3:
                row = atom.arguments[0].number
                col = atom.arguments[1].number
                value = atom.arguments[2].number

                sudoku[(row, col)] = value

        return cls(sudoku)
