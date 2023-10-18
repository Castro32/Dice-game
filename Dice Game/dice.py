import random


def roll_dice():
    return random.randint (1,6)
def main():
    while True:
        input("Press Enter to roll the dice.")
        result =roll_dice()
        print(f"You rolled a {result}")
        
        play_again=input("Do you want to play again? (yes/no):").lower()
        if play_again == "yes":
            input("Press Enter to roll the dice.")
            result =roll_dice()
            print(f"You rolled a {result}")
            break
        
        else:
            print("Thank You for playing!")
            break
if __name__ =="__main__":
    main()
    