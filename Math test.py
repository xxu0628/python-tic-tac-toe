import random
import time

def print_with_delay(message, delay=1):
    print(message)
    time.sleep(delay)

def get_user_input(prompt):
    return input(prompt)

def addition():
    score = 0
    for level in range(1, 4):
        for _ in range(10 if level == 1 else (30 if level == 2 else 100)):
            num1, num2 = random.randint(1, 10 * level), random.randint(1, 10 * level)
            answer = num1 + num2
            response = int(get_user_input(f"{num1} + {num2} = ? "))
            if response == answer:
                score += (1 if level == 1 else (2 if level == 2 else 4))
            else:
                print_with_delay(f"Wrong! The answer was {answer}. Current score: {score}")
                return score
    return score

def subtraction():
    score = 0
    for level in range(1, 4):
        for _ in range(10 if level == 1 else (30 if level == 2 else 110)):
            num1, num2 = random.randint(1, 10 * level), random.randint(1, 10 * level)
            answer = num1 - num2
            response = int(get_user_input(f"{num1} - {num2} = ? "))
            if response == answer:
                score += (1 if level == 1 else (2 if level == 2 else 4))
            else:
                print_with_delay(f"Wrong! The answer was {answer}. Current score: {score}")
                return score
    return score

def multiplication():
    score = 0
    for level in range(1, 4):
        for _ in range(20 if level == 1 else (60 if level == 2 else 140)):
            num1, num2 = random.randint(1, 10 * level), random.randint(1, 5 * level)
            answer = num1 * num2
            response = int(get_user_input(f"{num1} * {num2} = ? "))
            if response == answer:
                score += (2 if level == 1 else (4 if level == 2 else 8))
            else:
                print_with_delay(f"Wrong! The answer was {answer}. Current score: {score}")
                return score
    return score

def division():
    score = 0
    for level in range(1, 4):
        for _ in range(20 if level == 1 else (60 if level == 2 else 100)):
            num2 = random.randint(1, 20) + 1
            num1 = num2 * random.randint(1, 15)  # ensure divisibility
            answer = num1 // num2
            response = int(get_user_input(f"{num1} / {num2} = ? "))
            if response == answer:
                score += (2 if level == 1 else (4 if level == 2 else 4))
            else:
                print_with_delay(f"Wrong! The answer was {answer}. Current score: {score}")
                return score
    return score

def main():
    print_with_delay("Welcome to the Math Skill Tester!")
    print("When a problem appears, type in the answer and hit Enter.")
    
    while True:
        choice = get_user_input("Choose a section:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n> ")
        
        if choice == '1':
            score = addition()
        elif choice == '2':
            score = subtraction()
        elif choice == '3':
            score = multiplication()
        elif choice == '4':
            score = division()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        
        print(f"Your final score is {score}.")
        save_score = get_user_input("Do you want to save your score? (yes/no): ").lower()
        if save_score == 'yes':
            name = get_user_input("Please enter your name: ")
            with open("score.txt", "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d')} The player {name} has scored {score} points\n")

if __name__ == "__main__":
    main()
