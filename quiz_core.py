import json
import os
import random
import time
from colorama import init, Fore, Style
import pygame

init(autoreset=True)
pygame.mixer.init()


def play_sound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


SCORE_FILE = "scores.json"
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as score_file:
            return json.load(score_file)
    return {}


def save_scores(scores):
    with open(SCORE_FILE, "w") as score_file:
        json.dump(scores, score_file, indent=5)


def countdown(seconds=3):
    sound = pygame.mixer.Sound("start_quiz.wav")
    sound.play()
    for remaining_seconds in range(seconds, 0, -1):
        print(f"{Fore.YELLOW}⏳ The quiz will start in {remaining_seconds}...", end="\r")
        time.sleep(0.5)
    print(" " * 30, end="\r")


def load_questions(category):
    filename = f"{category}.txt"
    questions = []
    if not os.path.exists(filename):
        print(f"{Fore.RED}❌ The file '{filename}' is not found.")
        return questions
    with open(filename, "r") as file:
        for line in file:
            try:
                questions.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                print(f"{Fore.RED}❌ Invalid line")
    return questions


def list_categories():
    return [filename[:-4] for filename in os.listdir() if filename.endswith(".txt")]


def play_quiz():
    categories = list_categories()
    if not categories:
        print(f"{Fore.RED}❌ No categories found.")
        return

            
    print(f"{Fore.CYAN}🎮 Welcome to Quizzierett!🎮")
    players_name = input("Enter your name: ")
    if not players_name:
        print(f"{Fore.RED}❌ The name should not be empty.")
        return

        
    print("\nThe Categories are:")
    for index, catgry in enumerate(categories, 1):
        print(f"{index}.{catgry}")
    try:
        catgry_index = int(input("Choose a category (number only): ")) -1
        selected_category = categories[catgry_index]
    except (IndexError, ValueError):
        print(f"{Fore.RED}❌ Invalid choice!")
        return


    questions = load_questions(selected_category)
    if not questions:
        print(f"{Fore.RED}❌ No valid questions in this category.")
        return


    random.shuffle(questions)
    score = 0
    countdown()


    for question_file in questions:
        print(f"\n" + "~" * 50)
        print(f"{Fore.MAGENTA}{question_file['questions']}")
        for key, val in question_file["options"].items():
            print(f"{key.upper()}: {val}")


        users_answer = input("Your answer is: ")
        if users_answer.lower() == question_file["correct"]:
            play_sound("correct.wav")
            print(f"{Fore.GREEN}✅ Your answer is CORRECT!")
            score += 1
        else:
            play_sound("wrong.wav")
            print(f"{Fore.RED}❌ WRONG! The correct answer is {question_file['correct'].upper()}")


    print(f"{Fore.YELLOW}🎉 CONGRATULATIONS! You completed the quiz! \nYour score is: {score}/{len(questions)}")

    scores = load_scores()
    scores[players_name] = score
    save_scores(scores)

    print(f"{Fore.CYAN}🏆 Your score has been saved under the name '{players_name}.")


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
