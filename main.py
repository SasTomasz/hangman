import random

words = ['ELEPHANT', 'APPLE', 'CAR', 'DESTINATION', 'MINUTE']
word = ''
guessed_word = ''
wrong_guess = 0
game_over = False
points = 0

def draw_word(word): 
    guessed_word = ['_'] * len(word)
    words.remove(word)
    return guessed_word, word

""" 
word is word guessing by user
letter is letter give by user
returns new representation of guessing word with exposed letters 
"""
def check_letter(guessed_word, word, letter):
    is_letter_hit = 0
    global wrong_guess

    for x in range(len(word)):
       if word[x] == letter:
           guessed_word[x] = letter 
           is_letter_hit = 1
        
    if is_letter_hit == 0:
        wrong_guess += 1
        if wrong_guess < 3:
            print("This letter isn't in word. Try again")

    return guessed_word

def guessing_the_word(guessed_word, word):
    
    letter = ''

    while wrong_guess < 3:
        global points
        global game_over
        print('   '.join(guessed_word))
        letter = input("Guess the letter in the word: ").upper()
        guessed_word = check_letter(guessed_word, word, letter)
        if guessed_word.count('_') == 0:
            print("Good job, You guess the word: ", word)
            points += 1
            break

    if wrong_guess == 3:
        game_over = True
    pass

while wrong_guess < 3 and words != []:
    guessed_word, word = draw_word(random.choice(words))
    guessing_the_word(guessed_word, word)

if game_over == False:
    print("Congratulations. You win with %d points" %points)
else:
    print("Game Over. You have %d points" % points)




