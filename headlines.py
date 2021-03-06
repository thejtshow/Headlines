from sys import argv
from SolveHeadlineManually import *
from WordTree import *


# print out current headlines
def printHeadlines(headlines):
    C1, C2, C3, C4, C5 = headlines
    print('Headlines:\n{}\n{}\n{}\n{}\n{}\n'.format(C1[0],
                                                    C2[0],
                                                    C3[0],
                                                    C4[0],
                                                    C5[0]))


# get a headline choice
def pickHeadline(headlines):
    selected = None
    error = True
    C1, C2, C3, C4, C5 = headlines
    while(error):
        # print out all the headlines
        try:
            selected = eval('C' + input('Please pick a headline [1-5]: '))
            error = False
        except (NameError, IndexError):
            print('Incorrect choice. Try again.')
            error = True
    return selected


# print the sets of chains
def printChains(clues):
    for i, (_, chain) in enumerate(clues):
        print('{} -> {}'.format(i + 1, chain))
    input('Press Enter to continue...')


# initialization
def initialize():
    print('Building Word Tree...')
    tree = buildtree(argv[1])
    print('Done!\nGetting Clues from file...')
    C1, C2, C3, C4, C5 = [clue.strip() for i, clue
                          in enumerate(open(argv[2], 'r'))
                          if i < 5]  # only gets the first 5 lines of clues
    print('Done!')
    return [tree, [(C1, []), (C2, []), (C3, []), (C4, []), (C5, [])]]


# where shit happens
def main():
    tree, headlines = initialize()
    while True:
        printHeadlines(headlines)
        try:
            selection = int(input('What would you like to do?\n' +
                                  '1.\tSolve a Headline Manually\n' +
                                  '2.\tView Discovered Chains\n'
                                  '3.\tBuild a Matrix\n' +
                                  '4.\tReset a Headline and its Chains\n\n' +
                                  'Selection: '))
        except ValueError:
            print('Invalid selection, try again')
            continue
        # solve a headline manually
        if selection == 1:
            line = pickHeadline(headlines)
            solved = solveHeadline(tree, line[0])
            if solved is not None:
                # successfully solved a headline, update the headlines
                for i, headline in enumerate(headlines):
                    if headline[0] == line[0]:
                        headlines[i] = solved
                        break
                continue
        # View Discovered chains
        if selection == 2:
            printChains(headlines)
            continue
        # Build a matrix
        if selection == 3:
            continue
        # Reset a headline and its chains
        if selection == 4:
            continue


# make sure shit happens
if __name__ == '__main__':
    if len(argv) != 3:
        print('Usage: python headlines.py <dictionary> <clues>')
    else:
        main()
