import json

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self):
        print("\n" + self.question)
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option}")

        while True:
            try:
                choice = int(input("Wybierz numer odpowiedzi: "))
                if 1 <= choice <= len(self.options):
                    return self.options[choice - 1] == self.answer
                else:
                    print("⚠️ Podaj numer z zakresu odpowiedzi.")
            except ValueError:
                print("⚠️ Wpisz tylko liczbę.")

def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Question(q["question"], q["options"], q["answer"]) for q in data]

def save_score(score, total, filename="score.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Wynik: {score}/{total} ({round((score / total) * 100)}%)")

def main():
    print("=== Witaj w Quizie Naukowym! ===")
    questions = load_questions("questions.json")

    score = 0
    total = len(questions)

    for q in questions:
        if q.ask():
            print("✅ Dobrze!")
            score += 1
        else:
            print(f"❌ Źle! Poprawna odpowiedź: {q.answer}")

    wrong = total - score
    percent = (score / total) * 100

    print("\n=== Podsumowanie ===")
    print(f"Liczba pytań: {total}")
    print(f"Poprawnych: {score}")
    print(f"Błędnych: {wrong}")
    print(f"Twój wynik procentowy: {round(percent, 2)}%")

    save_score(score, total)

if __name__ == "__main__":
    main()