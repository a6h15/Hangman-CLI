import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def guessCorrect(placeholder, chosen_word, guess):
    placeholderList = list(placeholder)

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            placeholderList[i] = guess

    return ''.join(placeholderList)

word_list = ["bankai", "pokemon", "messi"]
chosen_word = random.choice(word_list)
print(f"{chosen_word}")

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

lives = 6


while "_" in placeholder and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        placeholder = guessCorrect(placeholder, chosen_word, guess)
        print(stages[lives])
    else:
        lives -= 1
        print(stages[lives])


    print(f"Current word: {placeholder}")

if "_" not in placeholder:
    print(f"Congratulations! You've guessed the word:{chosen_word}")
else:
    print(f"You lost!")
