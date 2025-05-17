import random

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = self._create_grid()
        self.hidden_grid = [['X'] * size for _ in range(size)]  # The grid shown to the player with 'X'

    def _create_grid(self):
        """Private method to create a new game grid with random pairs."""
        total_cells = self.size * self.size
        pairs = total_cells // 2
        numbers = list(range(pairs)) * 2
        random.shuffle(numbers)

        # Convert the list into a 2D grid
        return [numbers[i * self.size:(i + 1) * self.size] for i in range(self.size)]

    def display_grid(self, reveal=False):
        """Display the grid. If reveal=True, show actual values; otherwise, show hidden grid."""
        size = self.size

        # Print the column headers with [A] style
        column_headers = "    " + " ".join(f"[{chr(65 + i)}]" for i in range(size))
        print(column_headers)

        # Print each row with row labels in [0] style
        for i, row in enumerate(self.grid if reveal else self.hidden_grid):
            row_str = "  ".join(f"{cell:>2}" for cell in row)
            print(f"[{i}] {row_str}")

    def reveal_cells(self, row1, col1, row2=None, col2=None):
        """Reveals the values at the given coordinates."""
        self.hidden_grid[row1][col1] = self.grid[row1][col1]
        if row2 is not None and col2 is not None:
            self.hidden_grid[row2][col2] = self.grid[row2][col2]

    def reset_hidden_cells(self, row1, col1, row2=None, col2=None, permanently_revealed=None):
        """Resets non-matching cells back to 'X', unless they are permanently revealed."""
        if permanently_revealed is None:
            permanently_revealed = set()  # Default to an empty set if not provided

        # Reset cell 1 if not permanently revealed
        if (row1, col1) not in permanently_revealed:
            self.hidden_grid[row1][col1] = 'X'

        # Reset cell 2 if not permanently revealed
        if row2 is not None and col2 is not None and (row2, col2) not in permanently_revealed:
            self.hidden_grid[row2][col2] = 'X'
