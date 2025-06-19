import random

# Predefined list of words
word_list = ["apple", "tiger", "robot", "train", "green"]

# Choose a random word from the list
secret_word = random.choice(word_list)

# Track guessed letters
guessed_letters = []

# Display for the word with underscores
display_word = ["_"] * len(secret_word)

# Number of wrong attempts
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while wrong_guesses < max_wrong and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    guess = input("Enter a letter: ").lower()

    # Validate single letter
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess.")
        wrong_guesses += 1

# Game over
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game over! The word was:", secret_word)
