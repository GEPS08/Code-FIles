from genericpath import exists
import time
import os
import random
import english_words as words
from termcolor import colored
import PySimpleGUI as gui
# IMPORTING also remember to do | py -m pip install english-words | py -m pip install termcolor | py -m pip install pysimplegui

no_gui = ''

layout = [[gui.Text('Do you want to enable the gui?', font= ('Arial', 16))],
[gui.Button('Yes', size=(6, 1), font=('Arial', 32)), gui.Button('No', size=(6, 1), font=('Arial', 32))]]

window = gui.Window(title="Graphics options", layout=layout, size=(348, 140), element_justification='c')

while True:
    event, values = window.read()
    if event == 'Yes':
        enable_gui = 'true'
        window.close()
        break
    elif event == 'No':
        enable_gui = 'false'
        window.close()
        break
    elif event == gui.WIN_CLOSED:
        window.close()
        break

loop = 6
guess_number = 1

with open(r"C:\Users\Joe\.vscode\code files\wordle\5 letter words.txt", "r") as file:
    textfile = file.read()
    possible_words = list(map(str, textfile.split()))

random_num = random.randint(0,2499)

random_words_pos = possible_words[random_num]

wordle_word = random_words_pos

cyan = (colored('CYAN', 'grey', 'on_cyan'))
yellow = (colored('YELLOW', 'grey', 'on_yellow'))
red = (colored('RED', 'grey', 'on_red'))

wordle_word = ''.join(wordle_word)

if enable_gui == 'false':

    print ('\nif a letter is highlited in ' + cyan + ' then it in the correct place.\n')
    print ('if a letter is highlited in ' + yellow + ' then it is in the word but in the wrong place.\n')
    print ('if a letter is highlited in ' + red + ' then is is not in the word.\n\n')

    while loop > 0:

        guess_arr_pos1_col = ''
        guess_arr_pos2_col = ''
        guess_arr_pos3_col = ''
        guess_arr_pos4_col = ''
        guess_arr_pos5_col = ''

        guess_number = str(guess_number)

        guess = input('Guess number ' + guess_number + ':\n')

        wordle_word_arr = []
        guess_arr = []
    
        for letter in guess:
            guess_arr.append(letter)

        for letter in wordle_word:
            wordle_word_arr.append(letter)

        if len(guess_arr) == 5:
        
            if guess in possible_words:
                while loop > 0:

                    if guess_arr[0] == wordle_word_arr[0]:
                        guess_arr_pos1_col = 'on_cyan'
                    elif guess_arr[0] == wordle_word[4] or guess_arr[0] == wordle_word_arr[3] or guess_arr[0] == wordle_word_arr[2] or guess_arr[0] == wordle_word_arr[1]: 
                        guess_arr_pos1_col = 'on_yellow'
                    else:
                        guess_arr_pos1_col = 'on_red'

                    if guess_arr[1] == wordle_word_arr[1]:
                        guess_arr_pos2_col = 'on_cyan'
                    elif guess_arr[1] == wordle_word[4] or guess_arr[1] == wordle_word_arr[3] or guess_arr[1] == wordle_word_arr[2] or guess_arr[1] == wordle_word_arr[0]: 
                        guess_arr_pos2_col = 'on_yellow'
                    else:
                        guess_arr_pos2_col = 'on_red'

                    if guess_arr[2] == wordle_word_arr[2]:
                        guess_arr_pos3_col = 'on_cyan'
                    elif guess_arr[2] == wordle_word[4] or guess_arr[2] == wordle_word_arr[3] or guess_arr[2] == wordle_word_arr[1] or guess_arr[2] == wordle_word_arr[0]: 
                        guess_arr_pos3_col = 'on_yellow'
                    else:
                        guess_arr_pos3_col = 'on_red'

                    if guess_arr[3] == wordle_word_arr[3]:
                        guess_arr_pos4_col = 'on_cyan'
                    elif guess_arr[3] == wordle_word[4] or guess_arr[3] == wordle_word_arr[2] or guess_arr[3] == wordle_word_arr[1] or guess_arr[3] == wordle_word_arr[0]: 
                        guess_arr_pos4_col = 'on_yellow'
                    else:
                        guess_arr_pos4_col = 'on_red'

                    if guess_arr[4] == wordle_word_arr[4]:
                        guess_arr_pos5_col = 'on_cyan'
                    elif guess_arr[4] == wordle_word[3] or guess_arr[4] == wordle_word_arr[2] or guess_arr[4] == wordle_word_arr[1] or guess_arr[4] == wordle_word_arr[0]:
                        guess_arr_pos5_col = 'on_yellow'
                    else:
                        guess_arr_pos5_col = 'on_red'

                    guess_arr = ''.join(guess_arr)

                    display1 = (colored(guess_arr[0], 'grey', guess_arr_pos1_col))
                    display2 = (colored(guess_arr[1], 'grey', guess_arr_pos2_col))
                    display3 = (colored(guess_arr[2], 'grey', guess_arr_pos3_col))
                    display4 = (colored(guess_arr[3], 'grey', guess_arr_pos4_col))
                    display5 = (colored(guess_arr[4], 'grey', guess_arr_pos5_col))

                    print ('\n' + display1 + display2 + display3 + display4 + display5)

                    if guess == wordle_word:
                        print ('\nYou Win!\n\nThe word was ' + wordle_word + '\n')
                        loop = 0

                    guess_number = int(guess_number)
                    guess_number += 1
            
                    loop -= 1
                    break
                continue
            else:
                print('\nThis word is not on the list\n')
        else:
            print ('\nYour guess has to be a 5 letter word\n')
            continue
elif enable_gui == 'true':
    print ('\nnot done yet lol\n')



if loop == 0 and not guess == wordle_word:
    print ('\nYou Lose!\n\nThe word was ' + wordle_word + '\n')