#TODO 03 Give users three chances to ask wrong letter

import random

words = ['ELEPHANT', 'APPLE', 'CAR', 'DESTINATION', 'MINUTE']
word = ''
guessed_word = ''

def draw_word(word): 
    guessed_word = ['_'] * len(word)
    return guessed_word, word

""" 
word is word guessing by user
letter is letter give by user
returns new representation of guessing word with exposed letters 
"""
def check_letter(guessed_word, word, letter):
    for x in range(len(word)):
       if word[x] == letter:
           guessed_word[x] = letter 

    return guessed_word

def guessing_the_word(guessed_word, word):
    # wrong_guess = 0
    letter = ''
    win = False

    while win == False:
        print('   '.join(guessed_word))
        letter = input("Guess the letter in the word: ").upper()
        guessed_word = check_letter(guessed_word, word, letter)
        if guessed_word.count('_') == 0:
            win = True
            print("Congratulations, You guess word: ", word)
    pass


guessed_word, word = draw_word(random.choice(words))
guessing_the_word(guessed_word, word)



