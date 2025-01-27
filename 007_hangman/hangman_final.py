import random
from hangman_art import stages, logo
from hangman_words import word_list
import os


def screen_clear():
    '''Simple function to clear screen after each attempt.'''
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    screen_clear()

    if guess in display:
        print(f"You've already guessed {guess}.")
        print(display)
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n"
              + "Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print("You've guessed {guess}, that's not in the word. " +
              "You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
