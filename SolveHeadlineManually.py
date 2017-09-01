from WordTree import *


# try to start solving headlines
def solveHeadlines(tree, line):
    selected = makeTuple(line)
    print('selection: {}'.format(selected[1]))
    for i, word in enumerate(selected[0].split()):
        lst = getWords(tree, word)
        print('{} -> {} word possibilities'.format(i, len(lst)))


# make the clue into a tuple - readable format and one we can operate on
def makeTuple(clue):
    pair = ['', clue]
    for i, character in enumerate(clue):
        if character.isalpha():
            pair[0] += str(character)
        elif i == (len(clue) - 1) or not clue[i + 1].isalpha():
            continue
        else:
            pair[0] += ' '
    return pair


# get a list of all words that have the same pattern as the original
def getWords(tree, word):
    case = getPattern(word)
    return [possible for possible in generator(tree, len(word))
            if case == getPattern(possible)]  # only add if pattern matches


# return the character pattern of the given input word
def getPattern(word):
    currentLetter = 'A'
    seen = [''] * 26
    newWord = ''
    for letter in word:
        number = ord(letter) - 65
        if not seen[number]:
            seen[number] = currentLetter
            newWord += currentLetter
            currentLetter = chr(ord(currentLetter) + 1)
        else:
            newWord += seen[number]
    return newWord
