from colorama import init, Fore, Style

init(autoreset=True)

def main_menu():
    while True:
        print(f"\n{Fore.YELLOW}----- Quizzierett -----")
        print("1. Play Quiz")
        print("2. Exit")
        choice = input(f"{Fore.MAGENTA}Select an option: ")
        if choice == "1":
            play_quiz()
        elif choice == "2":
            print(f"{Fore.CYAN}Exiting..... Goodbye!👋")
            break
        else:
            print(f"{Fore.RED}❌ Invalid input!")


if __name__ == "__main__":
    main_menu()
