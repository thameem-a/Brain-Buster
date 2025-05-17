import os
import time
import sys
from grid import Grid

# Clear screen function
def clear_screen():
    os.system("clear")

# Title display
def display_title():
    print("------------------")
    print("|  Brain Buster  |")
    print("------------------")

# Display the menu
def display_menu():
    print("1. Let me select two elements")
    print("2. Uncover one element for me")
    print("3. I give up - reveal the grid")
    print("4. New game")
    print("5. Exit\n")

# Start a new game with a specified grid size
def start_new_game(grid_size):
    return Grid(grid_size)

# Calculate score based on the minimum and actual guesses
def calculate_score(min_guesses, actual_guesses):
    """Calculate score based on the minimum and actual guesses."""
    if actual_guesses == 0:
        return 0  # Avoid division by zero
    score = (min_guesses / actual_guesses) * 100
    return round(score)  # Return the rounded score as an integer

# Validate cell coordinates
def validate_coordinate(cell, grid_size):
    """Validate cell coordinates and provide specific error messages."""
    if len(cell) != 2:
        return False, "Invalid format. Use a letter followed by a number (e.g., A0)."

    column, row = cell[0].upper(), cell[1]

    # Check if the column is a letter and within range
    if not column.isalpha() or ord(column) - 65 < 0 or ord(column) - 65 >= grid_size:
        return False, "Column entry is out of range for this grid. Please try again."

    # Check if the row is a digit and within range
    if not row.isdigit() or int(row) < 0 or int(row) >= grid_size:
        return False, "Row entry is out of range for this grid. Please try again."

    return True, ""  # Coordinates are valid

def main():
    # Check if grid size is passed as a command-line argument
    if len(sys.argv) > 1:
        try:
            grid_size = int(sys.argv[1])
            if grid_size not in [2, 4, 6]:
                print("Invalid grid size. Defaulting to 4x4 grid.")
                grid_size = 4
        except ValueError:
            print("Invalid input. Please enter a valid integer for grid size. Defaulting to 4x4 grid.")
            grid_size = 4
    else:
        print("No grid size provided. Defaulting to 4x4 grid.")
        grid_size = 4

    game_grid = start_new_game(grid_size)
    pairs_found = 0
    total_pairs = (grid_size * grid_size) // 2
    min_guesses = total_pairs
    actual_guesses = 0
    uncovered_cells = set()  # Track cells uncovered in Option 2
    permanently_revealed = set()  # Track cells that are permanently visible
    used_option_1 = False  # Track if Option 1 was used at least once

    while True:
        clear_screen()
        display_title()
        game_grid.display_grid()
        display_menu()

        # Prompt for menu selection
        selection = input("Select: ").strip()


        if selection == "1":
            used_option_1 = True  # Mark that the player made a valid guess
            actual_guesses += 1  # Increment guesses for Option 1

            # Handle selecting two elements with input validation loop
            while True:
                cell1 = input("Enter first cell (e.g., A0): ").upper().strip()
                is_valid, error_message = validate_coordinate(cell1, grid_size)
                if not is_valid:
                    print("Input error:", error_message)
                    input("Press Enter to try again...")
                    continue

                cell2 = input("Enter second cell (e.g., A1): ").upper().strip()
                is_valid, error_message = validate_coordinate(cell2, grid_size)
                if not is_valid:
                    print("Input error:", error_message)
                    input("Press Enter to try again...")
                    continue

                # Check if the two cells are the same
                if cell1 == cell2:
                    print("You cannot select the same cell twice. Please try again.")
                    input("Press Enter to try again...")
                    continue

                # Both inputs are valid and different, break out of loop
                break

            # Extract row and column after validation
            row1, col1 = int(cell1[1]), ord(cell1[0].upper()) - 65
            row2, col2 = int(cell2[1]), ord(cell2[0].upper()) - 65

            # Reveal the selected cells
            game_grid.reveal_cells(row1, col1, row2, col2)
            clear_screen()
            display_title()
            game_grid.display_grid()

            # Pause to let the player view the revealed cells
            time.sleep(2)

            # Check if the cells match; if not, hide them again
            if game_grid.grid[row1][col1] != game_grid.grid[row2][col2]:
                game_grid.reset_hidden_cells(row1, col1, row2, col2, permanently_revealed)
            else:
                pairs_found += 1
                # Mark these cells as permanently revealed
                permanently_revealed.add((row1, col1))
                permanently_revealed.add((row2, col2))

            # Check if all pairs have been found right after the last match
            if pairs_found == total_pairs:
                clear_screen()
                display_title()
                game_grid.display_grid(reveal=True)
                score = calculate_score(min_guesses, actual_guesses)
                if not used_option_1 or (len(uncovered_cells) == grid_size * grid_size - 2):
                    print("You cheated – Loser! Your score is 0.")
                else:
                    print(f"Congratulations! You've won!! Your score is: {score}.")
                input("Ready to play again? Click Enter...")

                # Start a new game
                game_grid = start_new_game(grid_size)
                pairs_found = 0
                total_pairs = (grid_size * grid_size) // 2
                min_guesses = total_pairs
                actual_guesses = 0
                uncovered_cells = set()
                permanently_revealed = set()
                used_option_1 = False

        elif selection == "2":
            # Handle uncovering one element
            actual_guesses += 2  # Increment guess count by 2 for using Option 2

            while True:
                cell = input("Enter cell to uncover (e.g., A0): ").upper().strip()
                is_valid, error_message = validate_coordinate(cell, grid_size)
                if not is_valid:
                    print("Input error:", error_message)
                    input("Press Enter to try again...")
                    continue

                row, col = int(cell[1]), ord(cell[0].upper()) - 65
                if (row, col) in uncovered_cells or (row, col) in permanently_revealed:
                    print("This cell is already uncovered. Please select a different cell.")
                    input("Press Enter to try again...")
                    continue

                # If the input is valid and not already uncovered, break out of the loop
                break

            # Reveal the cell
            game_grid.reveal_cells(row, col, row, col)
            uncovered_cells.add((row, col))  # Track uncovered cell
            permanently_revealed.add((row, col))  # Permanently reveal this cell

            # Check if all cells have been uncovered using Option 2
            if len(uncovered_cells) == grid_size * grid_size:
                print("You cheated – Loser! Your score is 0.")
                input("Press Enter to return to the menu...")
                game_grid = start_new_game(grid_size)
                pairs_found = 0
                total_pairs = (grid_size * grid_size) // 2
                min_guesses = total_pairs
                actual_guesses = 0
                uncovered_cells = set()
                permanently_revealed = set()
                used_option_1 = False

        elif selection == "3":
            # Give up and reveal the grid
            clear_screen()
            display_title()
            game_grid.display_grid(reveal=True)
            print("\nReturning to the menu...")
            input("Press Enter to start a new game and return to the menu...")

            # Generate a new grid
            game_grid = start_new_game(grid_size)
            pairs_found = 0
            total_pairs = (grid_size * grid_size) // 2
            min_guesses = total_pairs
            actual_guesses = 0
            uncovered_cells = set()
            permanently_revealed = set()
            used_option_1 = False

        elif selection == "4":
            # Start a new game
            grid_size = int(input("Enter grid size (2, 4, or 6): "))
            if grid_size in [2, 4, 6]:
                game_grid = start_new_game(grid_size)
                pairs_found = 0
                total_pairs = (grid_size * grid_size) // 2
                min_guesses = total_pairs
                actual_guesses = 0
                uncovered_cells = set()
                permanently_revealed = set()
                used_option_1 = False
            else:
                print("Invalid grid size. Starting a 4x4 game by default.")
                game_grid = start_new_game(4)

        elif selection == "5":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

# Run the main game loop
if __name__ == "__main__":
    main()

