"""Projekt 2:Bulls & Cows"""

import random
import time

SEPARATOR = "-" * 47
DIGITS = 4
AMAZING_LIMIT = 5
AVERAGE_LIMIT = 10


def generate_secret() -> str:
    """Vytvoří tajné číslo s unikátními číslicemi, které nezačíná nulou."""
    secret = ""
    while len(secret) < DIGITS:
        digit = str(random.randint(0, 9))
        if secret == "" and digit == "0":
            continue
        if digit not in secret:
            secret += digit
    return secret


def check_guess(guess: str) -> str:
    """Vrátí text chyby v tipu, nebo prázdný řetězec, když je tip v pořádku."""
    if not guess:
        return "You didn't enter anything."
    for char in guess:
        if char not in "0123456789":
            return "Please enter only digits."
    if len(guess) != DIGITS:
        return f"The number must have exactly {DIGITS} digits."
    if guess[0] == "0":
        return "The number can't start with 0."
    if len(set(guess)) != DIGITS:
        return "Each digit can be used only once."
    return ""


def count_bulls(secret: str, guess: str) -> int:
    """Spočítá číslice, které jsou na správném místě."""
    bulls = 0
    for secret_digit, guess_digit in zip(secret, guess):
        if guess_digit == secret_digit:
            bulls += 1
    return bulls


def count_cows(secret: str, guess: str) -> int:
    """Spočítá číslice, které v čísle jsou, ale na jiném místě."""
    cows = 0
    for secret_digit, guess_digit in zip(secret, guess):
        if guess_digit != secret_digit and guess_digit in secret:
            cows += 1
    return cows


def word_form(count: int, singular: str, plural: str) -> str:
    """Vrátí slovo v jednotném nebo množném čísle (1 bull, 2 bulls)."""
    if count == 1:
        return singular
    return plural


def rating(guesses: int) -> str:
    """Ohodnotí hru podle počtu pokusů."""
    if guesses <= AMAZING_LIMIT:
        return "That's amazing!"
    if guesses <= AVERAGE_LIMIT:
        return "That's average."
    return "That's not so good."


def print_intro() -> None:
    """Vypíše úvodní text hry."""
    print(f"""{SEPARATOR}
I've generated a random {DIGITS} digit number for you.
Let's play a bulls and cows game.
{SEPARATOR}
Enter a number:
{SEPARATOR}""")


def play_game() -> int:
    """Odehraje jednu hru a vrátí počet pokusů."""
    secret = generate_secret()
    guesses = 0

    while True:
        guess = input(">>> ").strip()
        error = check_guess(guess)
        if error:
            print(error)
            print(SEPARATOR)
            continue

        guesses += 1
        bulls = count_bulls(secret, guess)
        cows = count_cows(secret, guess)
        if bulls == DIGITS:
            return guesses

        bull_word = word_form(bulls, "bull", "bulls")
        cow_word = word_form(cows, "cow", "cows")
        print(f"{bulls} {bull_word}, {cows} {cow_word}")
        print(SEPARATOR)


def ask_play_again() -> bool:
    """Zeptá se hráče, jestli chce hrát znovu."""
    while True:
        answer = input("Do you want to play again? (y/n): ").strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please enter y or n.")


def main() -> None:
    """Spustí hru a po každé hře nabídne další."""
    results = []
    print("Hi there!")

    while True:
        print_intro()
        start = time.perf_counter()
        guesses = play_game()
        seconds = round(time.perf_counter() - start)
        results.append(guesses)

        print("Correct, you've guessed the right number")
        guess_word = word_form(guesses, "guess", "guesses")
        print(f"in {guesses} {guess_word}!")
        print(f"It took you {seconds} seconds.")
        print(SEPARATOR)
        print(rating(guesses))
        print(f"Games played: {len(results)}, best game: {min(results)}")
        print(SEPARATOR)

        if not ask_play_again():
            print("Thanks for playing, bye!")
            break


if __name__ == "__main__":
    main()
