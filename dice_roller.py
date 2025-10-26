from random import randint

def dice_roller(user_input: str):
    user_input = user_input.replace(" ", "")
    rolls, d, sides = user_input.partition("d")

    rolls = int(rolls)
    sides = int(sides)

    results = []
    for _ in range(rolls):
        results.append(randint(1, sides))
    
    return results

def main():
    print("Simple Dice Roller")
    dice = input("Enter dice (e.g. 2d6): ")
    print("Rolling...")
    print(dice_roller(dice))

if __name__ == "__main__":
    main()
