import random

from possiblewords import words 


hangman = { 0: ("   ",
                "   ",
                "   "),
            1: (" o ",
                "   ",
                "   "),
            2: (" o ",
                " | ",
                "   "),
            3: (" o ",
                "/| ",
                "   "),
            4: (" o ",
                "/|\\",
                "   "),
            5: (" o ",
                "/|\\",
                "/  "),
            6: (" o ",
                "/|\\",
                "/ \\")}

def hangman_display(wrong_guesses):
    print("**********")
    for line in hangman[wrong_guesses]:
        print(line)
    print("**********")

def clue_display(clue):
    print(" ".join(clue))

def answer_display(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words).lower()
    clue = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    game_on = True

    while game_on:
        hangman_display(wrong_guesses)
        clue_display(clue)
        print()
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    clue[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in clue:
            hangman_display(wrong_guesses)
            answer_display(answer)
            print("YOU WIN!")
            game_on = False
        elif wrong_guesses >= len(hangman) - 1:
            hangman_display(wrong_guesses)
            answer_display(answer)
            print("YOU LOSE!")
            game_on = False
            
main()