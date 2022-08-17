# CS1210: HW3 version 1
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the intructional team.
#
def signed():
    return(["eplsn"])

######################################################################
# In this homework, you will build the internals for Boggle, a popular
# word game played with 16 6-sided dice. At the same time, in class we
# will develop the interactive user interface for Boggle, so that your
# solution, augmented with what we do in class, will give you a
# playable Boggle game. This assignment will also give us a chance to
# work on a system using the object-oriented paradigm.
#
# This is version 1 of the template file, which does not include the
# user interface.  I will periodically release updated versions, which
# you can then merge into your own code: still, be sure to follow the
# instructions carefully, so as to ensure your code will work with the
# new template versions that contain the GUI we develop in class.
#
# The rules of Boggle are available online. Basically, you will roll
# the dice and arrange them into a 4x4 grid. The top faces of the die
# will display letters, and your job is to find words starting
# anywhere in the grid using only adjacent letters (where "adjacent"
# means vertically, horizontally, and diagonally adjacent). In our
# version of Boggle, there are no word length constraints beyond those
# implicitly contained in the master word list.
#
# Although other dice configurations are possible, the original Boggle
# dice are (in no particular order):
D = ["aaeegn","abbjoo","achops","affkps","aoottw","cimotu","deilrx","delrvy",
     "distty","eeghnw","eeinsu","ehrtvw","eiosst","elrtty","himnqu","hlnnrz"]

# You will need sample() from the random module to roll the die.
from random import sample, randint

######################################################################
# Boggle is the base class for our system; it is analogous to the
# Othello class in our implementation of that game.  It contains all
# the important data elements for the current puzzle, including:
#    Boggle.board = the current puzzle board
#    Boggle.words = the master word list
#    Boggle.solns = the words found in the current puzzle board
#    Boggle.lpfxs = the legal prefixes found in the current puzzle board
# Additional data elements are used for the GUI and scoring, which
# will be added in subsequent versions of the template file.
#
# Note: we will opt to use Knuth's 5,757 element 5-letter word list
# ('words.dat') from the Wordnet puzzle, but the 113,809 element list
# of words from HW1 ('words.txt') should also work just as easily.
#
class Boggle ():
    # This is the class constructor. It should read in the specified
    # file containing the dictionary of legal words and then invoke
    # the play() method, which manages the game.
    def __init__(self, input='words.dat'):
        print('Weclome to Boggle!!')
        self.readwords(input)
        
        self.play()
        
    # Printed representation of the Boggle object is used to provide a
    # view of the board in a 4x4 row/column arrangement.
    def __repr__(self):
       
       
       s = ''
       for i in range(len(self.board)):
           for j in range(len(self.board[0])):
                s = s + self.board[i][j] + ' '
           s = s.strip() + '\n' 
       return s.strip().upper()   
   
    # The readwords() method opens the file specified by filename,
    # reads in the word list converting words to lower case and
    # stripping any excess whitespace, and stores them in the
    # Boggle.words list.
    def readwords(self, filename):
        f = open(filename, "r")
        self.words = f.read().lower().strip().split()
        f.close()
        print(len(self.words),'words read in from',filename)
        
        

    # The newgame() method creates a new Boggle puzzle by rolling the
    # dice and assorting them to the 4x4 game board. After the puzzle
    # is stashed in Boggle.board, the method also computes the set of
    # legal feasible word prefixes and stores this in Boggle.lpfxs.
    def newgame(self):
        Dice = sample(D,16)
        boggleChars = [x[randint(0, 5)]for x in Dice]
        
        self.board = [list(boggleChars[x:x+4]) for x in range(0,16,4)]
        
        possibleWords = [''.join(x) for x in self.words if len(set(''.join(list(x))) & set(boggleChars)) == len(set(''.join(list(x))))]
        
        self.lpfxs = set([x[:y+1] for x in possibleWords for y in range(len(x))])
        
        
       
    # The solve() method constructs the list of words that are legally
    # embedded in the given Boggle puzzle. The general idea is search
    # recursively starting from each of the 16 puzzle positions,
    # accumulating solutions found into a list which is then stored on
    # Boggle.solns.
    #
    # The method makes use of two internal "helper" functions,
    # adjacencies() and extend(), which perform much of the work.
    def solve(self):
        
        # Helper function adjacencies() returns all legal adjacent
        # board locations for a given location loc. A board location
        # is considered legal and adjacent if (i) it meets board size
        # constraints (ii) is not contained in the path so far, and
        # (iii) is adjacent to the specified location loc.
        def adjacencies(loc,path):
                  
            validLocs = set()
            if loc[0]+ 1 < 4:
                validLocs.add((loc[0]+1,loc[1]))
                down = True
            else:
                down = False
                
            if loc[0]- 1 >= 0: 
                validLocs.add((loc[0]-1,loc[1]))
                up = True
            else:
                up = False
                
            if loc[1]+ 1 < 4: 
                validLocs.add((loc[0],loc[1]+1))
                right =True
            else:
                right = False
                
            if loc[1]-1 >= 0:
                validLocs.add((loc[0],loc[1]-1))
                left =True
            else:
                left= False
            
            if up and left:
                validLocs.add((loc[0]-1,loc[1]-1))
            if up and right:
                validLocs.add((loc[0]-1,loc[1]+1))
            if down and left:
                validLocs.add((loc[0]+1,loc[1]-1))
            if down and right:
                validLocs.add((loc[0]+1,loc[1]+1))
                
            
            return list(validLocs - set(path))
            
          
       
        
        
        # Helper function extend() is a recursive function that takes
        # a location loc and a path traversed so far (exclusive of the
        # current location loc). Together, path and loc specify a word
        # or word prefix. If the word is in Boggle.words, add it to
        # Boggle.solns, because it can be constructed within the
        # current puzzle. Otherwise, if the curren prefix is still in
        # Boggle.lpfxs, attempt to extend the current path to all
        # adjacencies of location loc. To do this efficiently, a
        # particular path extension is abandoned if the current prefix
        # is no longer contained in self.lpfxs, because that means
        # there is no feasible solution to this puzzle reachable via
        # this extension to the current path/prefix.
        def extend(loc, path= []):
            for i in adjacencies(loc, path):
                word = self.extract(path)+self.board[loc[0]][loc[1]]
                if word in self.words:
                    self.solns.add(word)
                    
                if word in self.lpfxs:
                    path.append(loc)
                    extend(i,path)
                    path.pop()
                
           
        self.solns = set()
           
        for i in range(4):
            for j in range(4):
                extend((i,j),[]) 
             
        
        
        return self.solns

    # The extract() method takes a path and returns the underlying
    # word from the puzzle board.
    def extract(self, path):
        word = ''
        for i in range(len(path)):
            word = word + self.board[path[i][0]][path[i][1]]
        return word
        
        
    # The checkpath() method takes a path and returns the word it
    # represents if the path is legal (i.e., formed of distinct and
    # sequentially adjacent locations) and realizes a legal word,
    # False otherwise.
    def checkpath(self, path):
        for i in range(len(path)-1):
            
    
            if abs((path[i][0] - path[i+1][0]) + (path[i][1]-path[i+1][1]))==1 or (abs(path[i][0] - path[i+1][0])==1 and abs(path[i][1]-path[i+1][1])==1) :
                True
            else:
                return False
        if True:
            return self.extract(path)
            
    
    # The round() method plays a round (i.e., a single puzzle) of
    # Boggle. It should return True as long as the player is willing
    # to continue playing additional rounds of Boggle; when it returns
    # False, the Boggle game is over.
    #
    # Hint: Look to HW1's round() function for inspiration.
    #
    # This method will be replaced by an interactive version.
    def round(self):
        # The recover() helper function converts a list of integers
        # into a path. Thus '3 2 2 1 1 2 2 3' becomes [(3, 2), (2, 1),
        # (1, 2), (2, 3)].
        def recover(path):
             path =  path.replace(' ', '')
             path = [int(x) for x in path]
             return [tuple(path[x:x+2]) for x in range(0,(len(path)),2)] 
        
         
            
        self.newgame()
        sols  = self.solve()
        print(self)
        
        userAnswers = []
        
        while True:
            
            
            
            userInput = input('''Input 'r1 c1 r2 c2...'; '/'=display, ':'=show, '+'=new puzzle; '.'=quit >  ''')
            
            
        
            if userInput == '.':
                print('You found {} word(s): {} || There were {} possible solutions: {}'.format(len(userAnswers),userAnswers,len(sols),sols))
                return False
            elif userInput == '/':
                print(self)
                
            elif userInput == ':':
                print('you have found {} word(s)!'.format(len(userAnswers)))
                [print(x)for x in userAnswers]
            
            elif userInput == '+':
                print('You found {} word(s)! There were {} possible solutions: {}'.format(len(userAnswers),len(sols),sols))
                userAnswers=[]
                self.newgame()
                sols  = self.solve()
                print(self)
            
            else:
                try:
                    
                    word = self.checkpath(recover(userInput))
                    if not isinstance(word,str):
                        print('invalid path input')
                    else:
                        
                        if word in sols and word not in userAnswers:
                            print('Nice Job!!!')
                            print('you found the word {}!'.format(word.upper()))
                            userAnswers.append(word)
                        else:
                            print('Invalid Word')
                
                    
                except:
                    print('invalid input')
                
            

    # The play() method when invoked initiates a sequence of
    # individual Boggle rounds by repeatedly invoking the rounds()
    # method as long as the user indicates they are interested in
    # playing additional puzzles.
    #
    # Hint: Look to HW1's play() function for inspiration.
    #
    # This method will be replaced by an interactive version.
    def play(self):
        while self.round():
            self.round()

######################################################################
if __name__ == '__main__':
   Boggle()
   
