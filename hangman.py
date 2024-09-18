import random

def choose_word(word_list):
    """Chooses a random word from the given list."""
    return random.choice(word_list)

def initialize_game(word):
    """Initializes the game state."""
    return len(word) * "_"

def get_guess():
    """Gets a guess from the user."""
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        else:
            return guess

def update_game_state(word, guessed_letters, guess):
    """Updates the game state based on the guess."""
    new_state = []
    for letter in word:
        if letter in guessed_letters:
            new_state.append(letter)
        else:
            new_state.append("_")
    return "".join(new_state)

def check_win(game_state, word):
    """Checks if the game has been won."""
    return game_state == word

def check_lose(wrong_guesses):
    """Checks if the game has been lost."""
    return len(wrong_guesses) >= 7

def draw_hangman(wrong_guesses):
    """Draws the hangman based on incorrect guesses."""
    hangman_stages = [
        """
          |
          |
          |
          |
          |
        """,
        """
        -----
        |   |
            |
            |
            |
            |
        """,
        """
        -----
        |   |
        O   |
            |
            |
            |
        """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
        """,
        """
        -----
        |   |
        O   |
       /|   |
            |
            |
        """,
        """
        -----
        |   |
        O   |
       /|\  |
            |
            |
        """,
        """
        -----
        |   |
        O   |
       /|\  |
       /    |
            |
        """,
        """
        -----
        |   |
        O   |
       /|\  |
       / \  |
            |
        """
    ]

    return hangman_stages[len(wrong_guesses)]

def play_hangman():
    """Main game loop."""
    word_list = ["apple", "banana", "orange", "grape", "pear"]
    word = choose_word(word_list)
    game_state = initialize_game(word)
    guessed_letters = set()
    wrong_guesses = set()

    print("Welcome to Hangman!")
    print(game_state)

    while True:
        guess = get_guess()
        if guess in guessed_letters or guess in wrong_guesses:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            game_state = update_game_state(word, guessed_letters, guess)
            print(game_state)
            if check_win(game_state, word):
                print("Congratulations! You won.")
                break
        else:
            wrong_guesses.add(guess)
            print("Wrong guess. You have", 7 - len(wrong_guesses), "tries left.")
            print(draw_hangman(wrong_guesses))
            if check_lose(wrong_guesses):
                print("Game over! The word was:", word)
                break

if __name__ == "__main__":
    play_hangman()