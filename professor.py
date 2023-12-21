#a addition game with level digits and gives three chances and prints the score out of 10
import random

def main():
    digits = get_level()
    score = generate_integer(digits)
    print(score)

def get_level():# valid the level entered from the user which can be from 1 to 3
    while True:
        #run until the user enters 1, 2, or 3
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    start, end = 10**(level-1), 10**level-1

    total_score = 0
    for i in range(10): # for ten question

        a = random.randint(start, end)
        b = random.randint(start, end)
        answer = a + b
        answer_correct = False
        for i in range(3):# ask questions 3 times if not correct
            try:
                user_solution = int(input(f"{a} + {b} = "))
                if user_solution == answer:
                    total_score += 1
                    answer_correct = True
                    break

                else:
                    raise ValueError

            except ValueError:
                print("EEE")

        if not answer_correct:
            print(f"{a} + {b} = {answer}")

    return total_score


if __name__ == "__main__":
    main()
