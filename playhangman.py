import time
import numpy as np
import pandas as pd
import os
import random
from io import StringIO

def getAllWords():
    with open('hangman_words.txt') as words_txt:
        words_tuple = []
        for word in words_txt:
            words_tuple.append(word.strip('\n'))

    df = pd.DataFrame([words_tuple]).T
    df = df.rename(columns = {0: 'All Words'})
    return df

def getRandomWord():
    all_words_df = getAllWords()
    word = all_words_df.at[random.randint(0, 853), 'All Words']
    word = str(word)
    return word

def listToString(string):
    str1 = ''

    return(str1.join(string))

def playHangmanOnce():
    random_word = getRandomWord()
    word_string = '_ ' * len(random_word)
    underscores = [underscore for underscore in range(0, len(random_word) * 2) if underscore % 2 == 0]
    underscores[0] = 0
    guesses = 6
    guessed = False
    
    print('--- Hangman ---')
    print('Guess the word')
    print('You have {} chances to get the letter or word wrong'.format(guesses))
    print('Type "CTRL + C" to exit at any time')

    try:
        while guesses > 0 and guessed == False:

            print(' ')
            print(word_string)
            user = input('Guess a letter or word: ')
            
            user_in_word = [pos for pos, char in enumerate(random_word) if char == user]

            if len(user) > 1:
                if user == random_word:
                    print('You guessed the word!')
                    guessed = True
                else:
                    print("That's is not the word")
                    guesses -= 1
                    print('You have {} wrong guesses left'.format(guesses))
                    print(word_string)
            elif len(user) == 1:
                if len(user_in_word) == 1 and random_word.find(user) != -1 and word_string.find(user) == -1:
                    word_string = list(word_string)
                    word_string[underscores[user_in_word[0]]] = user
                    word_string = listToString(word_string)
                    
                    print(word_string)
                    
                    user_in_word.clear()
                elif len(user_in_word) > 1 and random_word.find(user) != -1 and word_string.find(user) == -1: 
                    word_string = list(word_string)
                    
                    for letter in range(0, len(user_in_word)):
                        word_string[underscores[user_in_word[letter]]] = user
                    
                    word_string = listToString(word_string)
                    
                    print(word_string)
                    
                    user_in_word.clear()
                elif word_string.find(user) != -1 :
                    print('You already guessed that letter')
                    print(word_string)
                else:
                    print('That letter is not in word!')
                    
                    guesses -= 1
                    
                    print('You have {} wrong guesses left'.format(guesses))
                    print(word_string)

            if word_string.find('_') == -1:
                print('You guessed the word!')
                
                guessed = True
            else:
                pass
        
        if guesses == 0:
            print('The word was ' + '"' + random_word + '"')
        else:
            pass
    
    except KeyboardInterrupt:
        print("\n Closed main game")

def main():
    keepPlaying = True

    while keepPlaying == True:
        playHangmanOnce()

        end = input('Would you like to keep playing? (y/n): \n')

        if end == 'y':
            pass
        elif end == 'n':
            print('Game successfully closed')
            keepPlaying = False
        else:
            print("I'll take that as a no")
            keepPlaying = False

main()
