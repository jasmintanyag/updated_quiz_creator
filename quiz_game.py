import random
from colorama import init, Fore, Style


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
