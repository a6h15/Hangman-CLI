import random

def guessCorrect(placeholder, chosen_word, guess):
    placeholderList = list(placeholder)

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            placeholderList[i] = guess

    return ''.join(placeholderList)

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

while "_" in placeholder:
    guess = input("Guess a letter: ").lower()
    placeholder = guessCorrect(placeholder, chosen_word, guess)
    print(f"{placeholder}")
