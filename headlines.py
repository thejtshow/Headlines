from sys import argv
from SolveHeadlineManually import *
from WordTree import *


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
