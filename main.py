def main():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input()

    match choice:
        case "1":
            print("You chose rock")
        case "2":
            print("You chose paper")
        case "3":
            print("You chose scissors")
        case _:
            print("Not a valid choice")

main()
