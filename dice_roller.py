from random import randint

SEPARATOR = "-" * 100
VALID_DICE = ["4", "6", "8", "10", "12", "20"]

def dice_roller(user_input: str):
    user_input = user_input.replace(" ", "").replace("'", "").replace('"', "")
    expression = [term.strip() for term in user_input.split('+') if term.strip()]

    if not expression:
        return "No dice specified.\n" + SEPARATOR, False

    dice = []
    for die in expression:
        rolls, d, sides = die.partition("d")
        if d != "d" or sides not in VALID_DICE:
            return "Invalid dice format or type.\n" + SEPARATOR, False

        rolls = int(rolls) if rolls else 1
        sides = int(sides)
        dice_rolls = [randint(1, sides) for _ in range(rolls)]
        dice.append(dice_rolls)

    result = ""
    for i, expr in enumerate(expression):
        rolls_str = ", ".join(str(x) for x in dice[i])
        total = sum(dice[i])
        result += f"{expr}: [{rolls_str}] (sum = {total})\n"

    return result.strip(), True

def main():
    print(SEPARATOR)
    print("Dice Roller - Now supports 'd6' shorthand!")
    print(SEPARATOR)
    while True:
        try:
            dice = input("Enter dice (Ctrl+C to exit): ")
            result, status = dice_roller(dice)
            print(result + "\n" + SEPARATOR)
        except KeyboardInterrupt:
            print("\nExiting Dice Roller. Goodbye!")
            break

if __name__ == "__main__":
    main()
