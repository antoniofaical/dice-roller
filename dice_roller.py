from random import randint

def dice_roller(user_input: str):
    user_input = user_input.replace(" ", "")
    expression = user_input.split("+")

    valid_dice = ["4", "6", "8", "10", "12", "20"]
    results = []

    for die in expression:
        rolls, d, sides = die.partition("d")
        if d != "d" or sides not in valid_dice:
            return "Invalid format or dice type", False

        rolls = int(rolls)
        sides = int(sides)

        result = [randint(1, sides) for _ in range(rolls)]
        results.append(result)

    formatted = ""
    for i, r in enumerate(results):
        formatted += f"{expression[i]}: {r}\n"

    return formatted, True

def main():
    print("Dice Roller")
    while True:
        user_input = input("Enter dice: ")
        result, status = dice_roller(user_input)
        print(result)
        if not status:
            continue

if __name__ == "__main__":
    main()
