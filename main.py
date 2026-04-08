import random

def main():
    options = ["Rock", "Paper", "Scissors"]
    while True:
        for option in options:
            print(f"{options.index(option) + 1}: {option}")
        choice = input()
        ai_choice = random.choice(options)

        

        match choice:
            case "1":
                if ai_choice == "Paper":
                    print("Ai chose paper you lose")
                elif ai_choice == "Scissors":
                    print("Ai chose scissors you win")
                else:
                    print("Its a tie")
            case "2":
                if ai_choice == "Scissors":
                    print("Ai chose Scissors you lose")
                elif ai_choice == "Rock":
                    print("Ai chose scissors you win")
                else:
                    print("Its a tie")
            case "3":
                if ai_choice == "Rock":
                    print("Ai chose Rock you lose")
                elif ai_choice == "Paper":
                    print("Ai chose paper you win")
                else:
                    print("Its a tie")
            case _:
                print("Not a valid choice")

main()
