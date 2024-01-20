def create_movies(filename):
    words = {}
    counter = 0
    with open(filename, encoding="utf8") as movies:
        for line in movies:
            number, movie = line.split(',')
            movie = movie.split('(')[0][:-1]
            if movie[-3:] == 'The':
                movie = 'The ' + movie[:-4]
            words[counter] = movie
            counter += 1
    return words

def create_HP_chars(filename):
    words = {}
    counter = 0
    with open(filename, encoding="utf8") as chars:
        for line in chars:
            words[counter] = line
            counter +=1
    return words

movies = create_movies("movies.txt")
HP_chars = create_HP_chars("Harry Potter Names.txt")

alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

from random import randint
def initialise():
    words = []
    while not words:
        choice = input('Enter \"M\"  for movies or Enter \"H\" for Harry Potter characters: ')
        if choice.upper() == 'M':
            words = movies
        elif choice.upper() == 'H':
            words = HP_chars
        else:
            print('Enter a valid letter.')
    index = randint(0, len(words) - 1)
    word = words.get(index)
    spaces = ''
    for char in word:
        if char.lower() in alphabet or char in numbers:
            spaces += '_'
        else:
            spaces += char
    return spaces, word

hang_man = [' ', '  |\n  |\n  |\n  |', '  |\n  |\n  |\n__|__', '  ____\n  |\n  |\n  |\n__|__',
            '  ____\n  |  O\n  |\n  |\n__|__', '  ____\n  |  O\n  |  |\n  |\n__|__', '  ____\n  |  O\n  | /|\ '[:-1] + '\n  |\n__|__',
            '  ____\n  |  O\n  | /|\ ' + '\n  | / \ ' + '\n__|__']

def hanged_man(count):
    return hang_man[count]

def edit_spaces(word, letter, spaces):
    for x in range(len(word)):
        if letter == word[x]:
            spaces = spaces[:x] + letter + spaces[x+1:]
    return spaces

def guess(word, letter, used, count, spaces):
    if len(letter) > 1:
        print('One letter at a time!')
    elif letter in used and len(letter) == 1:
        print('Used words: {}'.format(used))
        print('Oops! Letter already guessed, try again!')
    elif (letter in word or letter.upper() in word) and len(letter) == 1:
        used.append(letter)
        spaces = edit_spaces(word, letter, spaces)
        spaces = edit_spaces(word, letter.upper(), spaces)
        print('Correct!')
        print('Used words: {}'.format(used))
        print(spaces)
    elif len(letter) == 1:
        print('Incorrect!')
        used.append(letter)
        print('Used words: {}'.format(used))
        count += 1
        print(hanged_man(count))
        print(spaces)
    return used, count, spaces

def play():
    print('Playing Hangman: Movie edition.')
    used = []
    count = 0
    spaces, word = initialise()
    print(spaces)
    count = 0
    for something in word:
        if something in numbers:
            print('Remember that you can guess NUMBERS as well as LETTERS')
            break
    while '_' in spaces:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        letter = input('Enter a letter: ').lower()
        used, count, spaces = guess(word, letter, used, count, spaces)
        if count == len(hang_man)-1:
            break
    if '_' not in spaces:
        print('Congrats!')
    else:
        print('GAME OVER!!! \nThe movie was \"{}\".\nBetter Luck Next Time...'.format(word))

play()