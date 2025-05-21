from colorama import init, Fore, Style
from quiz_creator import QuizCreator
from quiz_game import QuizGame

init(autoreset=True)

class MainMenu:
    def __init__(self):
        self.creator = QuizCreator()
        self.game = QuizGame()

    def main_menu(self):
        while True:
            print(f"\n{Fore.YELLOW}----- Quizzierett -----")
            print("1. Play Quiz")
            print("2. Exit")
            choice = input(f"{Fore.MAGENTA}Select an option: ")
            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                print(f"{Fore.CYAN}Exiting..... Goodbye!👋")
                break
            else:
                print(f"{Fore.RED}❌ Invalid input!")

if __name__ == "__main__":
    menu = MainMenu()
    menu.main_menu()
