import random

class HangmanGame:
    def __init__(self):
        self.word_groups = {
            "Countries": [
                "ageria", "Qatar", "canada",  "egypt","moroco", "france"
            ],
            "Fruits": [
                "apple", "banana", "grape", "mango", "orange", "kiwi",
            ],
            "Technology": [
                "computer", "programming", "development", "algorithm"
            ],
            "Activities ": [
                "football", "travel","play guitar"
            ],
            "Foods and Desserts": [
                "chocolate"
            ],
            "Knowledge": [
                "science", "music", "challenge"
            ],
            "Programming Technology": [
                "python", "java"
            ]
        }

    def play(self):
        print("Welcome to Hangman!")
        print("Choose a category please:")

        categories = list(self.word_groups.keys())
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        try:
            chosen_index = int(input("Enter the number of the category: ")) - 1
            if chosen_index < 0 or chosen_index >= len(categories):
                raise ValueError
        except ValueError:
            print("Invalid input. Please restart the game and enter a valid number.")
            return

        chosen_category = categories[chosen_index]
        word_to_guess = random.choice(self.word_groups[chosen_category])
        guessed_letters = []
        attempts = 8

        print(f"chose the category: {chosen_category}.")
        print(f"You have {attempts} attempts to guess the word.")

        while attempts > 0:
            current_guess = ''.join(
                [letter if letter in guessed_letters else '_' for letter in word_to_guess]
            )
            print("\nCurrent word:", current_guess)

            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                guessed_letters.append(guess)
                attempts -= 1
                print("Wrong guess! Attempts left:", attempts)

            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"\nCongratulations! You guessed the word: {word_to_guess}")
                break
        else:
            print(f"\nSorry, you ran out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()
