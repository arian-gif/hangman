import random
import hangman_art
import hangman_words

# Game home page
print(hangman_art.logo)

# Initialize arrays
word_list = hangman_words.word_list
stages = hangman_art.stages

# Initialize game variables
chosen = random.choice(word_list)
display = "_" * len(chosen)
lives = 6
length = len(chosen)
guessed_letters = []

# Game loop
while length > 0 and lives > 0:
    print(display)
    print(stages[lives])
    print(f"**************************** {lives} LIVES LEFT ****************************")

    # Input validation using your logic
    allowable = False

    while not allowable:
        is_guess_valid = True
        guess = input("Take a guess:\n").lower()
        for letter in guessed_letters:
            if guess == letter:
                print("This guess is not acceptable, you already guessed it.")
                is_guess_valid = False
        if is_guess_valid:
            allowable = True
        else:
            allowable = False

    guessed_letters.append(guess)
    correct = False
    count = 0

    # Check guess
    for letter in chosen:
        if letter == guess:
            display = display[:count] + guess + display[count + 1:]
            correct = True
            length -= 1
        count += 1

    if not correct:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.\n")
        lives -= 1
    else:
        print("Correct!\n")

# End of game messages
if lives <= 0:
    print(f"\033[91mIT WAS '{chosen}'! YOU LOSE\033[0m")  # Red text
else:
    print("\033[92mYou win!\033[0m")  # Green text
