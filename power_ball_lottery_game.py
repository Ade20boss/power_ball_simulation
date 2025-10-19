from power_ball_ascii_art import logo
import random

# --- Global Constants ---
# Range for the 5 white balls (1 to 69)
WHITE_BALL_RANGE = (1, 69)
# Range for the single Powerball (1 to 26)
POWER_BALL_RANGE = (1, 26)
# Cost for one ticket
COST_PER_PLAY = 2
# Maximum number of plays allowed in a single entry
MAX_PLAYS = 1000000

# Dictionary mapping winning conditions to prize amounts.
# Key is a tuple: (number of white balls matched, Powerball matched - True/False)
prizes = {
    (5, True): "Jackpot",
    (5, False): 1000000,
    (4, True): 50000,
    (4, False): 100,
    (3, True): 100,
    (3, False): 7,
    (2, True): 7,
    (1, True): 4,
    (0, True): 4,
}


def get_white_ball_values():
    """
    Prompts the user to enter 5 unique white ball numbers.

    Validates that the input:
    1. Contains exactly 5 elements.
    2. Are all valid integers within the WHITE_BALL_RANGE (1-69).
    3. Are all unique numbers.

    Returns:
        set: A set containing the 5 user-selected white ball numbers.
    """
    while True:
        try:
            print("Enter 5 different numbers from 1 to 69, with a space between the numbers.")
            text = input("> ").split()

            if len(text) != 5:
                print("⚠️ Error: Please enter exactly 5 numbers.")
                continue

            # Convert to integers and validate range/uniqueness
            number_set = set()
            for s in text:
                num = int(s)  # Attempts to convert string to integer
                # Check if the number is within the defined range
                if not (WHITE_BALL_RANGE[0] <= num <= WHITE_BALL_RANGE[1]):
                    raise ValueError(f"Number {num} is outside the range {WHITE_BALL_RANGE}.")
                number_set.add(num)

            # Check for uniqueness (set size must equal 5)
            if len(number_set) < 5:
                print("⚠️ Error: You must enter 5 unique numbers.")
                continue

            return number_set
        except ValueError as e:
            # Catches errors from int() conversion or the range check
            print(f"⚠️ Invalid input: {e}. Please try again.")


def get_power_ball_number():
    """
    Prompts the user to enter the single Powerball number.

    Validates that the input:
    1. Is a valid integer.
    2. Is within the POWER_BALL_RANGE (1-26).

    Returns:
        int: The user-selected Powerball number.
    """
    while True:
        try:
            print("Enter the power ball number from 1 to 26.")
            text = input("> ")
            pb_number = int(text)  # Convert input to integer

            # Check if the number is within the defined range
            if not (POWER_BALL_RANGE[0] <= pb_number <= POWER_BALL_RANGE[1]):
                print(f"⚠️ You can't choose outside the range {POWER_BALL_RANGE}. Please try again.")
                continue

            return pb_number
        except ValueError:
            # Catches non-numeric input
            print("⚠️ Invalid input. Please enter a number.")


def get_and_calc_cost_of_play():
    """
    Prompts the user for the number of times they wish to play.

    Validates that the input:
    1. Is a positive integer.
    2. Does not exceed MAX_PLAYS.
    Also calculates and prints the total cost.

    Returns:
        int: The number of plays the user selected.
    """
    while True:
        try:
            print("How many times do you want to play? (Max: 1,000,000) ")
            print("Cost per play is $2")
            times_to_play = int(input("> "))

            # Validation checks
            if times_to_play == 0:
                print(f"You should at least play once.")
                continue
            if times_to_play > MAX_PLAYS:
                print(f"You can only play {MAX_PLAYS:,} times per entry.")
                continue

            # Calculate and print total cost
            print(f"It costs ${times_to_play * COST_PER_PLAY:,} to play {times_to_play:,} times. Good luck!")
            return times_to_play
        except ValueError:
            # Catches non-numeric input
            print("⚠️ Invalid input. Please enter a whole number.")


def get_winning_values():
    """
    Generates a set of 5 unique winning white ball numbers and one winning Powerball number.

    Returns:
        tuple: (winning_set, winning_power_ball_number)
            winning_set (set): 5 unique numbers from WHITE_BALL_RANGE.
            winning_power_ball_number (int): 1 number from POWER_BALL_RANGE.
    """
    winning_set = set()
    # Generate the winning Powerball
    winning_power_ball_number = random.randint(POWER_BALL_RANGE[0], POWER_BALL_RANGE[1])
    # Generate 5 unique white balls
    while len(winning_set) < 5:
        number = random.randint(WHITE_BALL_RANGE[0], WHITE_BALL_RANGE[1])
        winning_set.add(number)
    return winning_set, winning_power_ball_number


def check_wins():
    """
    Runs the Powerball simulation for the selected number of plays.

    1. Gets user numbers and play count.
    2. Loops through the number of plays, generating winning numbers each time.
    3. Calculates the number of matches.
    4. Looks up the prize based on the match key in the 'prizes' dictionary.
    5. Accumulates total winnings and prints the result of each draw.
    6. Prints a final summary of total winnings or loss.
    """
    # Get user's chosen numbers
    white_ball_values = get_white_ball_values()
    power_ball_value = get_power_ball_number()
    # Get play count and calculate cost
    times_to_play = get_and_calc_cost_of_play()

    win_value = ""
    count = 0
    total = 0  # Total accumulated winnings
    win_or_lose = "You won"

    print()
    print("Press any key to continue...")
    input()

    # Loop for each game played
    for _ in range(times_to_play):
        count = 0  # Reset match count for each draw
        winning_values, winning_power_ball_value = get_winning_values()

        # Check white ball matches
        for i in white_ball_values:
            if i in winning_values:
                count += 1

        # Create the key for the prizes dictionary: (white_matches, powerball_matched)
        key = (count, power_ball_value == winning_power_ball_value)

        if key in prizes:
            win_or_lose = "You won"
            win_value = prizes[key]

            # Add prize to total
            if isinstance(win_value, int):
                total += win_value
            elif win_value == "Jackpot":
                # Using a fixed large amount for the Jackpot in this simulation
                total += 400000000
        else:
            win_or_lose = "You lose"
            win_value = "0"

        # Print result of the current draw
        print(
            f"The winning numbers are: {winning_values} and powerball value is: {winning_power_ball_value} \t{win_or_lose}")

    # --- Final Summary ---
    if total > 0:
        print("Thank you for playing!")
        # Print total winnings, formatted with commas
        print(f"You won ${total:,}")
        return
    else:
        print("Thank you for playing!")
        # Print total money spent (loss)
        print(f"You just wasted ${times_to_play * 2}")


def main():
    """
    Main function to run the Powerball game loop.

    Continuously prints the logo, runs a round of the game (check_wins),
    and prompts the user to play again.
    """
    while True:
        print(logo)  # Display the Powerball ASCII art logo
        check_wins()  # Run the main game simulation

        # Ask user if they want to play another round
        replay = input("Do you want to play again? (y/n) ")

        if replay.lower() == "y":
            continue  # Start a new round
        else:
            print("Thank you for playing!")
            exit()  # Exit the program


main()