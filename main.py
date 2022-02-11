#TODO 03 Give users three chances to ask wrong letter
#TODO 04 When user guess letter all that letter shows out

import random

def draw_word(word): 
    guessing_word = ['_'] * len(word)
    return guessing_word

def guessing_the_word(word):
    print('   '.join(word))
    pass

words = ['Elephant', 'Apple', 'Car', 'Destination', 'Minute']
guessing_word = draw_word(random.choice(words))

guessing_the_word(guessing_word)



