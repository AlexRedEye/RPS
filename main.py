import random

def main():
    options = ["Rock", "Paper", "Scissors"]
    wins = 0
    losses = 0
    ties = 0

    while True:
        print(f"Wins: {wins} | Losses: {losses} | Ties: {ties}")
        for option in options:
            print(f"{options.index(option) + 1}: {option}")
        choice = input()
        ai_choice = random.choice(options)

        

        match choice:
            case "1":
                if ai_choice == "Paper":
                    print("Ai chose paper you lose")
                    losses += 1
                elif ai_choice == "Scissors":
                    print("Ai chose scissors you win")
                    wins += 1
                else:
                    print("Its a tie")
                    ties += 1
            case "2":
                if ai_choice == "Scissors":
                    print("Ai chose Scissors you lose")
                    losses += 1
                elif ai_choice == "Rock":
                    print("Ai chose scissors you win")
                    wins += 1
                else:
                    print("Its a tie")
                    ties += 1
            case "3":
                if ai_choice == "Rock":
                    print("Ai chose Rock you lose")
                    losses += 1
                elif ai_choice == "Paper":
                    print("Ai chose paper you win")
                    wins += 1
                else:
                    print("Its a tie")
                    ties += 1
            case _:
                print("Not a valid choice")

main()
