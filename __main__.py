from hangman import Hangman

import time
import sys


# Colors for screen text
RED = '\u001b[31;1m'
BLUE = '\u001b[34;1m'
YELLOW = '\u001b[33;1m'
GREEN = '\u001b[39;1m'
LEMON = '\u001b[32;1m'


def main():

    try:

        game = Hangman()
        # Load words from file
        game.load_words()

        while True:
            game.set_starter()
            game.set_showword()
            # Reset lives and wrongs every round
            game.lives = 8
            game.wrong_guess = []

            print(GREEN)
            play = input('Do you want to play? (y/n): \n> ')

            if play == 'y':

                round = 1

                time.sleep(1)

                while '?' in game.show_word and game.lives > 0:

                    print(GREEN, '------------------------------------------')
                    print(YELLOW, f'\nRound: {round}')
                    print(BLUE, f'\nYour word: {"".join(game.show_word)}\n')

                    print(LEMON, f'You have {game.lives} lives.\n')
                    print(RED, f'Wrong guesses: {game.wrong_guess}')

                    print(GREEN)
                    letter = game.take_input()
                    if game.char_check(letter) == True:
                        game.true_char()
                    else:
                        game.false_char()

                    print(''.join(game.show_word))

                    print(GREEN, '-------------------------------------------\n\n')

                    round += 1

                if game.lives != 0:
                    print(YELLOW, 'Congrats, you won! :) \n')
                else:
                    print(RED, 'You lost! :( \n')

            else:
                print(GREEN, '\nCiao!')
                time.sleep(1)
                sys.exit(0)

    except IndexError:
        print(GREEN, '\n No more words..\n')
        print('Quitting..\n')
        time.sleep(1)
        sys.exit(0)

    except KeyboardInterrupt:
        print(GREEN, '\n\nQuitting..\n')
        time.sleep(1)
        sys.exit(0)


if __name__ == '__main__':

    main()