import random

word_list = ["apple", "tiger", "plant", "stone", "chair"]
chosen_word = random.choice(word_list)
guessed_letters = []
max_attempts = 6
wrong_guesses = 0

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("_ " * len(chosen_word))

while wrong_guesses < max_attempts:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try a new one.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Good guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess! Remaining attempts:", max_attempts - wrong_guesses)

    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word.strip())

    if all(letter in guessed_letters for letter in chosen_word):
        print("Congratulations! You guessed the word:", chosen_word)
        break

if wrong_guesses == max_attempts:
    print("Game over. The word was:", chosen_word)
    print("Thank you for playing.")
