from random import randint

SEPARATOR = "-" * 100
VALID_DICE = ["4", "6", "8", "10", "12", "20"]

def dice_roller(user_input: str):
    """
    Parses a dice expression (e.g., '2d6 + 1d8') and rolls the specified dice.
    Returns a formatted string with results and a status boolean.
    """
    # Normalize input
    user_input = user_input.replace(" ", "").replace("'", "").replace('"', "")

    # Split expression (supports multiple dice rolls separated by '+')
    expression = [term.strip() for term in user_input.split('+') if term.strip()]

    # Validation
    if not expression:
        return "No dice specified.\n" + SEPARATOR, False

    dice = []
    for die in expression:
        number_of_rolls, d, sides = die.partition("d")
        if d != "d":
            return (
                "All dice rolls must follow the format {n}d{sides}\n" + SEPARATOR,
                False,
            )
        if sides not in VALID_DICE:
            return (
                "Please specify valid dice: [d4, d6, d8, d10, d12, d20]\n" + SEPARATOR,
                False,
            )

        # Handle cases like "d6" → 1d6
        number_of_rolls = int(number_of_rolls) if number_of_rolls else 1
        sides = int(sides)

        # Roll dice
        dice_rolls = [randint(1, sides) for _ in range(number_of_rolls)]
        dice.append(dice_rolls)

    # Format output
    result_lines = []
    for i, expr in enumerate(expression):
        rolls_str = ", ".join(str(x) for x in dice[i])
        total = sum(dice[i])
        result_lines.append(f"{expr}: [{rolls_str}] (sum = {total})")
    
    result = "\n".join(result_lines)
    return result, True


def main():
    """Main program loop for the Dice Roller CLI."""
    print(SEPARATOR)
    print("\nWelcome to the Dice Roller! This program helps you quickly roll RPG dice!")
    print("Valid dice:\n\t[d4, d6, d8, d10, d12, d20]")
    print("Usage examples:")
    print("\tRoll 2 four-sided dice →  '2d4'")
    print("\tRoll 1 six-sided and 1 eight-sided die →  '1d6 + 1d8'\n")
    print(SEPARATOR, "\n")

    while True:
        try:
            dice = input("Enter the dice to roll (Ctrl+C to exit): ")
            result, status = dice_roller(dice)
            print("\n" + result + "\n")
            if status:
                print(SEPARATOR + "\n")
        except KeyboardInterrupt:
            print("\n\n", SEPARATOR + "\n\nExiting Dice Roller. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
