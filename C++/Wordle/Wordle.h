///////////////////////////////////////////////////////////////////
//
// Programmer: Eli Paulsen
// Date: Feb 16, 2022
// Name: Wordle.h
// Description: Wordle class header file, initializes public/private
//              variables and methods.
///////////////////////////////////////////////////////////////////

#include <string>
#include <vector>
#include <fstream>
#ifndef HW2_WORDLE_H
#define HW2_WORDLE_H
using namespace std;


class Wordle {
public:
    explicit Wordle(string file = ""){                      //Wordle class constructor
        setFile(file);                                       //calls setter for file name
        srand  (time(nullptr));                             //sets seed to use rand()

        for(int i=0; i<26; i++){
            availableLetter[i] = true;                      //sets whole array to true
        }
    }
    string getFile() const;                     //File getter method
    void setFile(string file);                  //file setter method
    void loadWordList();                        //file load/ read in method
    void printWordList();                       // print word list method
    string getSecretWord() const;               //secret word getter method
    void setSecretWord(string newSecret);       //secret word setter method
    void setRandomSecretWord();                 //random secret word setter method
    int getGuessNum();                          //guess number getter method
    bool makeGuess(string guess);               //method that tests guess with secret word
    void print();                               //prints out guesses and feedback
    void printAvailableLetters();               //prints our available letters

private:
    string wordListFilename;                //name of file
    vector<string> wordList;                //vector with all words in txt file
    string secretWord;                      //secret word
    int guessNum = 0;                       // number of guesses
    const int MAX_GUESS_NUM = 6;            // maximum number of guesses
    vector<string> guesses;                   // list of previous guesses
    vector<string> feedback;                 // list of feedback strings
    bool availableLetter[26];               //array of bools corresponding to whether or not letter is available
    string albet{"abcdefghijklmnopqrstuvwxyz"};     //alphabet string
};


#endif //HW2_WORDLE_H
