# ─────────────────────────────────────────────────────────────
#  HANGMAN GAME  —  Python Console Version
# ─────────────────────────────────────────────────────────────
 
import random
 
# ── STEP 1: Predefined word list ──────────────────────────────
WORDS = ["python", "hangman", "keyboard", "javascript", "variable"]
MAX_WRONG = 6
 
# ── STEP 2: Hangman ASCII art (0 wrong → 6 wrong) ─────────────
HANGMAN_STAGES = [
    # 0 wrong guesses
    """
  +---+
  |   |
      |
      |
      |
      |
=========
    """,
    # 1 wrong guess — head
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
    """,
    # 2 wrong guesses — head + body
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    """,
    # 3 wrong guesses — head + body + left arm
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    """,
    # 4 wrong guesses — head + body + both arms
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
    """,
    # 5 wrong guesses — head + body + both arms + left leg
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
    """,
    # 6 wrong guesses — full body (DEAD)
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
    """,
]
 
 
# ── STEP 3: Display the current word with blanks ──────────────
def display_word(word, guessed_letters):
    """Show guessed letters; replace un-guessed ones with _"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
 
 
# ── STEP 4: Display game status ───────────────────────────────
def display_status(wrong_count, wrong_letters, word, guessed_letters):
    print(HANGMAN_STAGES[wrong_count])
    print(f"  Wrong guesses: {wrong_count}/{MAX_WRONG}")
    print(f"  Missed letters: {', '.join(sorted(wrong_letters)) or 'none'}\n")
    print("  Word: " + display_word(word, guessed_letters))
    print()
 
 
# ── STEP 5: Get a valid single letter from the player ─────────
def get_guess(guessed_letters):
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("  ⚠  Please enter exactly one letter.")
        elif not guess.isalpha():
            print("  ⚠  Only letters are allowed.")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess
 
 
# ── STEP 6: Main game function ────────────────────────────────
def play_hangman():
    # Pick a random word
    word = random.choice(WORDS)
 
    guessed_letters = []   # all letters the player has tried
    wrong_letters   = []   # only the incorrect ones
 
    print("\n" + "=" * 40)
    print("       W E L C O M E  T O  H A N G M A N")
    print("=" * 40)
    print(f"  The word has {len(word)} letters. Good luck!\n")
 
    # ── Main game loop ────────────────────────────────────────
    while True:
        wrong_count = len(wrong_letters)
 
        # Show current state
        display_status(wrong_count, wrong_letters, word, guessed_letters)
 
        # ── Check win condition ───────────────────────────────
        if all(letter in guessed_letters for letter in word):
            print("  🎉  YOU WIN!  The word was:", word.upper())
            print("=" * 40 + "\n")
            break
 
        # ── Check lose condition ──────────────────────────────
        if wrong_count >= MAX_WRONG:
            print("  💀  GAME OVER!  The word was:", word.upper())
            print("=" * 40 + "\n")
            break
 
        # Get the player's guess
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)
 
        # Check if guess is correct
        if guess in word:
            print(f"\n  ✅  '{guess}' is in the word!\n")
        else:
            wrong_letters.append(guess)
            remaining = MAX_WRONG - len(wrong_letters)
            print(f"\n  ❌  '{guess}' is NOT in the word. "
                  f"{remaining} guess(es) remaining.\n")
 
 
# ── STEP 7: Play again loop ───────────────────────────────────
def main():
    while True:
        play_hangman()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye. 👋\n")
            break
 
 
# ── Entry point ───────────────────────────────────────────────
if __name__ == "__main__":
    main()