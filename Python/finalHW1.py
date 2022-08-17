# CS1210: HW1
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the intructional team.
#
def signed():
    return(["eplsn"])

######################################################################
# In this homework, you will be implementing a spelling bee game,
# inspired by the that appears in the New York Times. The purpose of
# the game is to find as many possible words from a display of 7
# letters, where each word must meet the following criteria:
#   1. it must consist of four or more letters; and
#   2. it must contain the central letter of the display.
# So, for example, if the display looks like:
#    T Y
#   B I L
#    M A
# where I is the "central letter," the words "limit" and "tail" are
# legal, but "balmy," "bit," and "iltbma" are not.
#
# We'll approach the construction of our system is a step-by-step
# fashion; for this homework, I'll provide specs and function
# signatures to help you get started. If you stick to these specs and
# signatures, you should soon have a working system.
#
# First, we'll need a few functions from the random module. Read up on
# these at docs.python.org.
from random import choice, randint, sample

######################################################################
# fingerprint(W) takes a word, W, and returns a fingerprint of W
# consisting of an ordered set of the unique character constituents of
# the word. You have already encountered fingerprint(W) so I will
# provide the reference solution here for you to use elsewhere.
def fingerprint(W):
    return(''.join(sorted(set(W))))

######################################################################
# score(W) takes a word, W, and returns how many points the word is
# worth. The scoring rules here are straightforward:
#   1. four letter words are worth 1 point;
#   2. each additional letter adds 1 point up to a max of 9; and
#   3. pangrams (use all 7 letters in display) are worth 10 points.
# So, for example:
#      A L
#     O B Y
#      N E
#   >>> score('ball')
#   1
#   >>> score('balloon')
#   4
#   >>> score('baloney')
#   10     # Pangram!
#
'''
Full Points
'''
def score(W):

    if len(W) == 4:
        print('nice! +1 point')
        return 1

    elif len(W) > 4:
        if len(fingerprint(W))==7:                      #pangram
            print('!pangram! +10 points')
            return 10

        elif len(W)-4+1 <= 9:
            print('awesome! +',len(W)-4+1,' points')
            return len(W)-4+1

        elif len(W)-4+1 >9:
            print('incredible! +9 points')
            return 9

    else:
        print('words must be 4 characters long to be scored.')





######################################################################
# jumble(S, i) takes a string, S, having exactly 7 characters and an
# integer index i where 0<=i<len(S). The string describes a puzzle,
# while i represents the index of S corresponding to the "central"
# character in the puzzle. This function doesn't return anything, but
# rather prints out a randomized representation of the puzzle, with
# S[i] at the center and the remaining characters randomly arrayed
# around S[i]. So, for example:
#    >>> jumble('abelnoy', 1)
#     A L
#    O B Y
#     N E
#    >>> jumble('abelnoy', 1)
#     N Y
#    L B A
#     E O
#
'''
-1 returns something other than None 
'''
def jumble(S, i):
    S = (list(S.upper()))
    c = S.pop(i)                                     # pops out character that will be in center of puzzle
    S = sample(fingerprint(S),len(fingerprint(S)))   # randomizes the rest of the puzzle


    print('  ',S[0],' ',S[1],'\n',
          S[2],' ',c,' ',S[3],'\n',                  # displays puzzle
          ' ',S[4],' ',S[5],'\n')

    return ''.join(S+list(c)).lower(), c.lower()        # returns characters in puzzle and center letter


#jumble('abelnoy', 3)

######################################################################
# readwords(filename) takes the name of a file containing a dictionary
# of English words and returns two values, a dictionary of legal words
# (those having 4 or more characters and fingerprints of 7 or fewer
# characters), with fingerprints as keys and values consisting of sets
# of words with that fingerprint, as well as a list, consisting of all
# of the unique keys of the dictionary having exactly 7 characters (in
# no particular order).
#
# Your function should provide some user feedback. So, for example:
#    >>> D,S=readwords('words.txt')
#    113809 words read: 82625 usable; 33830 unique fingerprints.
#    >>> len(S)
#    13333
#    >>> S[0]
#    'abemort'
#    >>> D[S[0]]
#    {'barometer', 'bromate'}
#
'''
Full Points
'''
def readwords(filename):

    f = open(filename, "r")
    wordbank = f.read().split()
    f.close()
    usable = [x.lower() for x in wordbank if len(x) >= 4 and len(fingerprint(x)) <= 7]              #creates a subset of usable words out of wordbank

    worddict = {fingerprint(v):set() for v in usable}
    print(len(wordbank),' words read: ',len(usable),' usable; ',len(worddict),' unique fingerprints')

    for word in usable:
        worddict[fingerprint(word)].add(word)                   #adds words to the dictionary when they share the same fingerprint as the key

    keys = [x for x in worddict.keys() if len(x)== 7]

    return worddict, keys



######################################################################
# round(D, S) takes two arguments, corresponding to the values
# returned by readwords(), randomly selects a puzzle seed from the
# list S and a central letter from within S. It then shows the puzzle
# and enters a loop where the user can:
#    1. enter a new word for scoring;
#    2. enter / to rescramble and reprint the puzzle;
#    3. enter + for a new puzzle; or
#    4. enter . to end the game.
# When a word is entered, it is checked for length (must be longer
# than 4 characters and its fingerprint must be contained within the
# puzzle seed). The word is then checked against D, and if found, is
# scored and added to the list of words.
#
# Here is a sample interactive transcript of round() in action:
#    >>> D,S = readwords('words.txt')
#    >>> round(D,S)
#     E H
#    R P U
#     O S
#    Input words, or: '/'=scramble; ':'=show; '+'=new puzzle; '.'=quit
#    sb> pose
#    Bravo! +1
#    sb> repose
#    Bravo! +3
#    sb> house
#    Word must include 'p'
#    sb> :
#    2 words found so far:
#      pose
#      repose
#    sb> \
#     H R
#    O P E
#     S U
#    sb> prose
#    Bravo! +2
#    sb> +
#    You found 3 of 415 possible words: you scored 6 points.
#    True
#
'''
Full Points
'''
def round(D, K):

    i = 0
    while i == 0:
        j=0
        puzzle,center = (jumble(K[randint(0,len(K)-1)],randint(0,6)))  # takes in information from the puzzle
        answers = []
        scores = []

        while j == 0:

            print(''' Input words, or: '/'=scramble; ':'=show; '+'=new puzzle; '.'=quit ''')

            userinput = input().lower()

            usable = [x for y in D.values() for x in y]
            puzzleSols = [x for x in usable if set(x) | set(puzzle) == set(puzzle) and center in x]  # list of all words that can be created with the current puzzle

            if userinput == '.':
                print('you scored ',sum(scores),' points on this puzzle\n')
                print(len(answers),'out of ',len(puzzleSols),' possible words\n')
                print('\t Thanks for playing ;)')

                i = 1
                j = 1    # out of both loops

            elif userinput == '+':
                print('you scored ',sum(scores),' points on this puzzle')

                print(len(answers),'out of ',len(puzzleSols),' possible words')

                j = 1  #out of inner loop

            elif userinput == ':':
                print(len(answers),' words found so far:\n', '\n '.join(answers))

            elif userinput == '/':
                jumble(puzzle,puzzle.index(center))             # shuffles the current puzzle
            else:
                if any(userinput in value for value in D.values()):            # checks if input is in dictionary of usable words
                    if userinput not in answers:                    # checks if word was answered already

                        if userinput in puzzleSols:
                            scores.append(score(userinput))             # list of scores
                            answers.append(userinput)                   # list of answers already guessed
                        else:
                            print('use only the charcters in the puzzle, must include center letter')
                    else:
                        print('you already guessed',userinput)
                else:
                    print('enter a valid word')





######################################################################
# play(filename='words.txt') takes a single optional argument filename
# (defaults to 'words.txt') that gives the name of the file containing
# the dictionary of legal words. After invoking readwords(), it
# repeatedly invokes rounds() until it obtains a False, indicating the
# game is over.
#

'''
-1 fails to repeatedly call round() until returns False
    -Expected something like: 
        while(round(D,K)): 
            pass
'''
def play(filename='words.txt'):
    print('Welcome to the spelling bee! \n\t   Good Luck!')
    D,K = readwords(filename)
    round(D,K)



'''
STYLE AND FORMAT

Full points
'''



####################################################################


######################################################################
# AutoGrader Feedback
######################################################################
######################################################################
### Your final score will be posted on ICON. Just FYI, the point	
### breakdown is:	
###    score()      4 points	
###    jumble()     3 points	
###    readwords() 12 points	
###    round()     11 points	
###    play()       4 points	
###    style        6 points	
### Total          40 points	
######################################################################
######################################################################

'''

**********************************************************************
File "../hw1test.py", line 9, in __main__
Failed example:
    jumble('acghotu', 6)
Expected:
     O H
    A U G
     C T
Got:
       O   H 
     A   U   G 
       C   T 
    <BLANKLINE>
    ('ohagctu', 'u')
**********************************************************************
File "../hw1test.py", line 14, in __main__
Failed example:
    jumble('acghotu', 0)
Expected:
     C U
    H A O
     T G
Got:
       C   U 
     H   A   O 
       T   G 
    <BLANKLINE>
    ('cuhotga', 'a')
**********************************************************************
File "../hw1test.py", line 19, in __main__
Failed example:
    score('orthodoxy')
Expected:
    10
Got:
    !pangram! +10 points
    10
**********************************************************************
File "../hw1test.py", line 22, in __main__
Failed example:
    score('aardvarks')
Expected:
    6
Got:
    awesome! + 6  points
    6
**********************************************************************
File "../hw1test.py", line 25, in __main__
Failed example:
    score('ilia')
Expected:
    1
Got:
    nice! +1 point
    1
**********************************************************************
File "../hw1test.py", line 28, in __main__
Failed example:
    score('cinnamiciac')
Expected:
    9
Got:
    awesome! + 8  points
    8
**********************************************************************
1 items had failures:
   6 of  11 in __main__
***Test Failed*** 6 failures.
'''

### Hawkid: eplsn
### TestScore: 5
######################################################################
### This concludes the Autograder output. The TestScore shown above
### does not contribute to your final grade, rather only provides
### the TAs who are grading your code with some preliminary guidance.
######################################################################
