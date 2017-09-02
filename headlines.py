from sys import argv
from SolveHeadlineManually import *
from WordTree import *


# get a headline choice
def pickHeadline(headlines):
    selected = None
    error = True
    C1, C2, C3, C4, C5 = headlines
    while(error):
        # print out all the headlines
        print('{}\n{}\n{}\n{}\n{}\n'.format(C1, C2, C3, C4, C5))
        try:
            selected = eval('C' + input('Please pick a headline [1-5]: '))
            error = False
        except (NameError, IndexError):
            print('Incorrect choice. Try again.')
            error = True
    return selected


# initialization
def initialize():
    print('Building Word Tree...')
    tree = buildtree(argv[1])
    print('Done!\nGetting Clues from file...')
    C1, C2, C3, C4, C5 = [clue.strip() for i, clue
                          in enumerate(open(argv[2], 'r'))
                          if i < 5]  # only gets the first 5 lines of clues
    print('Done!')
    return (tree, (C1, C2, C3, C4, C5))


# where shit happens
def main():
    tree, headlines = initialize()
    while True:
        try:
            selection = int(input('What would you like to do?\n' +
                                  '1.\tSolve a Headline Manually\n' +
                                  '2.\tView Discovered Chains\n'
                                  '3.\tBuild a Matrix\n' +
                                  '4.\tReset a Headline and its Chains\n'))
        except ValueError:
            print('Invalid selection, try again')
            continue
        if selection == 1:
            solved = solveHeadline(tree, pickHeadline(headlines))
            continue
        if selection == 2:
            continue
        if selection == 3:
            continue
        if selection == 4:
            continue


# make sure shit happens
if __name__ == '__main__':
    if len(argv) != 3:
        print('Usage: python headlines.py <dictionary> <clues>')
    else:
        main()
