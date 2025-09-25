import random


# 1. level auswählen - alles was nicht 1-3 ist reprompt
# 2 frage ausgeben - 3 chancen zur beantworten - ansosnten wird richtige antwort ausgegeben
# 3. nachdem alle fragen durch sind score ausgeben und programm beenden


def main():
    score = 0
    difficulty = get_level()
    #wrong_answers = 0

    # 10 aufgaben werden gestellt mit jeweils 3 versuchen
    for problem in range(10):

        wrong_answers = 0
        x = generate_integer(difficulty)
        y = generate_integer(difficulty)
        result = x + y
        guess = input(f'{x} + {y} = ')
        guess = int(guess)

        while True:
            if guess == result:
                score = score + 1
                break
            else:
                wrong_answers = wrong_answers + 1
                if wrong_answers != 3:
                    print("EEE")
                    guess = input(f'{x} + {y} = ')
                    guess = int(guess)
                    continue

                if wrong_answers == 3:
                    print(result)

                    break
        continue

    # for schleife und spiel vorbei
    print(score)

# fordert eingabe und returned level difficulty
def get_level():
#prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3

        #akzeptiert nur dei eingaben 1, 2 und 3
        while True:
            try:
                level_n = input("Level: ")
                level_n = int(level_n)
                if level_n not in [1, 2, 3]:
                    raise ValueError
                else:
                    return level_n

            # wenn nicht 1, 2 oder 3 reprompt
            except ValueError:
                continue

# bestimmt wie die level schwierigkeit ummgesetzt wird
def generate_integer(level):
    #returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3
    if level == 1:
        X = random.randint(0, 9)
    elif level == 2:
        X = random.randint(10, 99)
        #X = int(X)
    elif level == 3:
        X = random.randint(100, 999)
        #X = int(X)
    return X



if __name__ == "__main__":
    main()
