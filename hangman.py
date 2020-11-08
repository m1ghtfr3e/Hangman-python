# TODO:
# 2 Game progress
# 3 Time limit
# 4 Choose levels
# 5 Make game more editable


import random


class Hangman():
    
    PATH = './assets/'
    WORDS = []

    def __init__(self):
        self.lives = 8
        self.starter = ''
        self.char = ''
        self.show_word = []
        self.wrong_guess = []

    @classmethod
    def load_words(cls):

        lang = input('\nChoose your language (ger/en/fr): \n> ')
        if lang == 'ger':
            text_file = cls.PATH + 'german.txt'
        if lang == 'fr':
            text_file = cls.PATH + 'french.txt'
        if lang == 'en':
            text_file = cls.PATH + 'english.txt'

        with open(text_file, 'r') as f:
            for word in f.readlines():
                cls.WORDS.append(word.strip('\n').lower())

        # Make sure, there are no duplicates
        cls.WORDS = list(set(cls.WORDS))

    def set_starter(self):

        random.shuffle(self.WORDS)
        choice = random.choice(self.WORDS)
        self.WORDS.remove(choice)
        
        # Remove german "umlaut"
        if 'ä' in choice:
            choice = choice.replace('ä', 'ae')
        if 'ö' in choice:
            choice = choice.replace('ö', 'oe')
        if 'ü' in choice:
            choice = choice.replace('ü', 'ue')
        if 'ß' in choice:
            choice = choice.replace('ß', 'ss')

        # Remove french accents
        if 'é' in choice:
            choice = choice.replace('é', 'e')
        if 'è' in choice:
            choice = choice.replace('è', 'e')

        self.starter = choice

    def set_showword(self):
        self.show_word = ['?' for char in self.starter]

    def get_lives(self):
        return self.lives

    def take_input(self):
        char = str(input('Letter: \n> '))

        self.char = char
        return char

    def char_check(self, c):
        if c in self.starter:
            return True
        else:
            self.wrong_guess.append(c)
            return False

    def false_char(self):
        self.lives -= 1
        return 'You lost 1 live.'

    def true_char(self):
        ''' 
            If char is in 
            word, we replace
            it;
        '''
        indexes = []
        for i, j in enumerate(self.starter):
            if j == self.char:
                indexes.append(i)

        for index in indexes:
            self.show_word[index] = self.char
