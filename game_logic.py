import random
from ascii_art import STAGES



def get_random_word():
    words = ["python", "git", "github", "snowman", "meltdown"]
    secret_word = random.choice(words)
    return secret_word


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_"
    print("Secret word:", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = 3

    print("Welcome to Snowman Meltdown!")
    #For now, display the initial game state
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < max_mistakes:
        guess = input("Guess a letter: ").lower()
        # not needed to check if type is str because the input always gives a string back
        if type(guess) != str:
            print("Invalid input. Please enter a single letter.")

        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")

        else:
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            if guess in secret_word:
                guessed_letters.append(guess)
                print("Excellent guess!")
            else:
                mistakes += 1
                print("Wrong guess!")

            display_game_state(mistakes, secret_word, guessed_letters)

            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You guessed the word right!")
                break

    else:
        print(f"Game over! The word was {secret_word}. Good luck next time!")

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again == "y":
        play_game()
    elif play_again == "n":
        print("Thanks for playing!")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")



if __name__ == "__main__":
    play_game()