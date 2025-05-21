import json
import os
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
