from sys import argv


# object in the tree
class Node(object):
    def __init__(self, word=None):
        self.word = word
        self.children = {}


# generator for words
def generator(tree, length):
    for child in tree.children.values():
        if child.word is not None and len(child.word) == length:
            yield child.word
        yield from generator(child, length)


# add a word to a tree
def addWord(tree, word):
    current = tree
    for i, letter in enumerate(word):
        try:
            current = current.children[letter]
        except KeyError:
            current.children[letter] = Node(word=word
                                            if i == (len(word) - 1) else None)
            current = current.children[letter]


# build a tree from a dictionary file
def buildtree(file):
    tree = Node()
    for line in open(file, 'r'):
        addWord(tree, line.rstrip().upper())
    return tree


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


# get a headline choice
def pickHeadline(C1, C2, C3, C4, C5):
    selected = None
    error = True
    while(error):
        # print out all the headlines
        print('{}\n{}\n{}\n{}\n{}\n'.format(C1, C2, C3, C4, C5))
        try:
            selected = eval('C' + input('Please pick a headline [1-5]: '))
            error = False
        except NameError:
            print('Incorrect choice. Try again.')
            error = True
    return selected


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


# try to start solving headlines
def solveHeadlines(tree, line):
    selected = makeTuple(line)
    print('selection: {}'.format(selected[1]))
    for i, word in enumerate(selected[0].split()):
        lst = getWords(tree, word)
        print('{} -> {} word possibilities'.format(i, len(lst)))


# where shit happens
def main():
    print('Building Word Tree...')
    tree = buildtree(argv[1])
    print('Done!\nGetting Clues from file...')
    C1, C2, C3, C4, C5 = [clue.strip() for i, clue
                          in enumerate(open(argv[2], 'r'))
                          if i < 5]  # only gets the first 5 lines of clues
    print('Done!')
    line = pickHeadline(C1, C2, C3, C4, C5)
    solveHeadlines(tree, line)


# make sure shit happens
if __name__ == '__main__':
    if len(argv) != 3:
        print('Usage: python headlines.py <dictionary> <clues>')
    else:
        main()
