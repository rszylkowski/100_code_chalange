"""
Hangman game
"""

import random
import os
from hangman_art import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list)
display = ['_' for e in chosen_word]
lives = len(stages) -1
num_letters = len(display)
print(logo)
print(stages[lives])
print("Guess the word\n" + " ".join(display) + "\n")
guess_letter_list = []


while lives > 0 and num_letters > 0:

    guess_letter = input("Guess a letter: ").lower()
    while not len(guess_letter) == 1:
        print("Invalid input. Enter one letter.")
        guess_letter = input("Guess a letter: ").lower()

    if guess_letter in guess_letter_list:
        print("You've already type this letter. Try again.")
        continue

    os.system("cls")
    print(logo)
    guess_letter_list.append(guess_letter)

    for index, letter in enumerate(chosen_word):
        if letter == guess_letter:
            display[index] = letter.lower()
            num_letters -= 1
    if guess_letter not in chosen_word:
        lives -= 1
        print(f"\nThe letter you selected \"{guess_letter}\" is not in the word. You lose a life.")

    print(stages[lives])
    print(" ".join(display))

if "_" not in display:
    print("You Win!!!")
else:
    print("You Lose!!!")
