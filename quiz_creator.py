import json
from colorama import init, Fore, Style
from quiz_core import QuizCore

init(autoreset=True)

class QuizCreator(QuizCore):
    def create_quiz_file(self):
        print(f"\n{Fore.CYAN} ✨ Welcome to Quiz Creation!✨")
        print(f"{Fore.YELLOW}(Type 'exit' anytime to quit.)\n")

        category = input(f"{Fore.CYAN}📁 Enter a quiz category: ").lower().strip()
        if not category or category == 'exit':
            return
    
        filename = f"{category}.txt"
        questions = []

        while True:
            questn = input(f"{Fore.CYAN}📝 Enter a question: ")
            if questn.lower() == 'exit':
                break

            options = {}
            for choice in ['a', 'b', 'c', 'd']:
                answers = input(f"{Fore.YELLOW}🔹 Option {choice}: ")
                if answers.lower() == 'exit':
                    return
            
                options[choice] = answers

            correct_ans = input(f"{Fore.CYAN}Enter the CORRECT answer (a, b, c, d): ").lower().strip()
            print(f"{Fore.YELLOW}Received input: {correct_ans}") #debugging line
            while correct_ans not in ['a', 'b', 'c', 'd']:
                correct_ans = input(f"{Fore.RED}❌ INVALID. Choose only from (a, b, c, d): ").lower().strip()

                print(f"{Fore.YELLOW}You entered: {correct_ans}")

            questions.append({
                "questions": questn,
                "options": options,
                "correct": correct_ans})
        
            print(f"{Fore.GREEN}🎉 Question added!")
        
        with open(filename, "a") as f:
            for entry in questions:
                f.write(json.dumps(entry) + "\n")
    
        print(f"{Fore.GREEN}✨ All questions are now saved in {filename} under the {category} category.✨")

if __name__ == "__main__":
    quiz_creator = QuizCreator()
    quiz_creator.create_quiz_file()
