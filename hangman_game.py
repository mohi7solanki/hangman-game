from hangman_pics import HANGMANPICS
from pyfiglet import Figlet
import random, os
import subprocess


def print_game_intro():
    f = Figlet(font='standard')
    print()
    print(f.renderText('hanngman'))

    print(HANGMANPICS[6])

    f = Figlet(font='contessa')
    print(f.renderText('Welcome to hangman game!'))

def fill(word, c, char_indices):
    for i in char_indices:
        word[i] = c
    return word


def fill_letter(word, characters):
    new_word = word
    for c in characters:
        char_indices = [i for i, j in enumerate(random_word) if j == c]
        new_word = fill(new_word,c,char_indices)
    return new_word

def clear_screen():
    subprocess.call(["printf", "'\033c'"])
    display_word  = list(len(random_word)*'_')
    print_game_intro()
    print('Guess the word: {}'.format(' '.join(display_word)))


def main():
    print_game_intro()
    words = open('hangman_words.txt').read().splitlines()
    global random_word
    random_word = list(random.choice(words).upper())
    display_word  = list(len(random_word)*'_')
    print('Guess the word: {}'.format(' '.join(display_word)))
    user_input_list = []
    error_count = 0
    while error_count <= 5:
        user_input = input('Answer: ').upper()
        if user_input in random_word and user_input not in user_input_list:
            user_input_list.append(user_input)
            display_word = fill_letter(display_word, user_input_list)
            if display_word == random_word:
                print('\nWell Done!')
                break
        else:
            #print(HANGMANPICS[error_count])
            error_count += 1
        clear_screen()
        if error_count > 0:
            print(HANGMANPICS[error_count])
        print(' '.join(display_word))
    else:
        print('\nYou are HANGED, the word was: {}'.format(' '.join(random_word)))

if __name__ == '__main__':
    main()
