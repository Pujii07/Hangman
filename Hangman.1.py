import random

words = ["apple", "tiger", "house", "chair"]
word = random.choice(words)

guessed = "_" * len(word)
chances = 5

print("Welcome to Hangman")

while chances > 0 and guessed != word:

    print("\nWord:", guessed)
    letter = input("Enter a letter: ")

    new_guessed = ""

    for i in range(len(word)):
        if word[i] == letter or guessed[i] != "_":
            new_guessed += word[i]
        else:
            new_guessed += "_"

    if new_guessed == guessed:
        chances -= 1
        print("Wrong guess")
    else:
        print("Correct guess")

    guessed = new_guessed
    print("Chances left:", chances)

if guessed == word:
    print("\nYou won! The word is:", word)
else:
    print("\nYou lost! The word was:", word)