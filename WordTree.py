# object in the tree
class Node(object):
    def __init__(self, word=None):
        self.word = word
        self.children = {}


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


# generator for words
def generator(tree, length):
    for child in tree.children.values():
        if child.word is not None and len(child.word) == length:
            yield child.word
        yield from generator(child, length)
