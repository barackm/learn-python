import random
questions = [
    {
        "title": "What is the chemical symbol for water?",
        "choices": [
            "A: O2",
            "B: H2O",
            "C: CO2",
            "D: HO"
        ],
        "answer": "B",
    },
    {
        "title": "Which planet is known as the Red Planet?",
        "choices": [
            "A: Venus",
            "B: Earth",
            "C: Mars",
            "D: Jupiter"
        ],
        "answer": "C",
    },
    {
        "title": "What gas do plants absorb from the atmosphere?",
        "choices": [
            "A: Oxygen",
            "B: Carbon dioxide",
            "C: Nitrogen",
            "D: Helium"
        ],
        "answer": "B",
    },
    {
        "title": "Which element is necessary for the process of photosynthesis?",
        "choices": [
            "A: Nitrogen",
            "B: Carbon",
            "C: Chlorophyll",
            "D: Phosphorus"
        ],
        "answer": "C",
    },
    {
        "title": "What is the center of an atom called?",
        "choices": [
            "A: Nucleus",
            "B: Electron",
            "C: Proton",
            "D: Neutron"
        ],
        "answer": "A",
    }
]

def main():
    random.shuffle(questions) 
    correct_answers_count= 0
    
    for index, question in enumerate(questions, start=1):
        print(f"Question: {index}: {question["title"]}")
        for choice in question["choices"]:
            print(choice)
        answer = input("Your answer: ").upper()
        
        if answer == question["answer"]:
            print("\033[1;32mCorrect!\033[0m\n")
            correct_answers_count += 1
        else:
            print(f"\033[1;31mWrong! The correct answer is {question["answer"].upper()}\033[0m\n")
        
    print(f"\n\nQuiz over! Your final score is {correct_answers_count} out of {len(questions)}")


if __name__ == "__main__":
    main()