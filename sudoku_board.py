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
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        row = 0

        for line in s.splitlines():
            cells = line.split()

            if not cells:
                continue

            row += 1

            for col, value in enumerate(cells, start=1):
                if value != "-":
                    sudoku[(row, col)] = int(value)

        return cls(sudoku)
