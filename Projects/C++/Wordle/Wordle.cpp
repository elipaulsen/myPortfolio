////////////////////////////////////////////////////////////////////
//
// Programmer: Eli Paulsen
// Date: Feb 16, 2022
// Name: Wordle.cpp
// Description: Wordle class. defines methods that can be used on
//              wordle objects.
///////////////////////////////////////////////////////////////////

#include "Wordle.h"

void Wordle::setFile(string file) {
    wordListFilename = file;                // sets file to be read in as wordList filename
}

string Wordle::getFile() const {
    return wordListFilename;                // returns filename
}

void Wordle::loadWordList() {
    ifstream fin(wordListFilename);         //opens filename

    if (fin.is_open()){

        int numWords = 0;
        string line;
        while (getline(fin, line)) {            //reads in number of words in the wordlist
            numWords++;
        }
        fin.clear();
        fin.seekg(0, fin.beg);              // resets the file to be read in
        wordList.resize(numWords);              // resizes vector to hold all words

        int j = 0;
        while(!fin.eof()){
            getline(fin,wordList[j]);           // reads in words into vector wordList
            j++;
        }
        fin.close();                                //close file

    }
    else{
        cout << endl << "ERROR: Could not open " << wordListFilename << endl;       //prints error if file can't be found
    }
}

void Wordle::printWordList() {                              //prints all words in the vector wordList
    for(int i=0; i<wordList.size(); i++){
        cout << wordList[i] << endl;
    }
    if(wordList.empty()){                                     //if no words in wordList print out warning
        cout << "WARNING: Word list is empty" << endl;
    }
}

string Wordle::getSecretWord() const {
    return secretWord;                      //returns secretWord variable
}

void Wordle::setSecretWord(string word) {
    if (find(wordList.begin(),wordList.end(),word) == wordList.end()){          //sets secret word as arguement passed into method
        cout << word << " is not in word list" << endl;                                    //if word is in wordlist
    }
    else {
        secretWord = word;
    }

}

void Wordle::setRandomSecretWord() {
    if(!wordList.empty()){
        secretWord = wordList[rand() % wordList.size()];        //sets secretWord to be a random word in vector wordList
    }
}

int Wordle::getGuessNum() {                                 //getter that returns the number of guesses the user has made
    return guessNum;
}

bool Wordle::makeGuess(string guess) {
    if (find(wordList.begin(), wordList.end(), guess) == wordList.end()) {          //if guess is in wordlist
        cout << "Invalid guess: " << guess << " is not in " << wordListFilename << endl;
        cout << "Please make different guess." << endl;
    }
    else {
        guesses.push_back(guess);           //add guess to guesses vector
        string fBack = ".....";
        string copyOfSecret = secretWord;

        //check if letter is in correct location
        for(int i=0; i<5; i++){
            if(guess.at(i)==copyOfSecret.at(i)){
                fBack.at(i) = '!';
                copyOfSecret.at(i) = '-';
            }
        }

        //checks if letter is somewhere in word
        for(int i=0; i<5; i++){
            if(fBack.at(i)!='!'){
                for(int j=0; j<5; j++){     //checks each letter in guess with every letter in secret word
                    if(guess.at(i)==copyOfSecret.at(j)){
                        fBack.at(i) = '+';
                        copyOfSecret.at(j) = '-';
                    }
                }
            }
        }

        //sets letters to false if no letter is in secret word
        for(int i=0; i<5; i++){         //loop thru guess
            if(fBack.at(i) == '.'){       //if letter is not in word
                availableLetter[albet.find(guess.at(i))] = false;       //set array slot corresponding to the letter to false
            }
        }

        //fixes double letter glitch
        for(int i=4; i>=0; i--){         //loop thru guess
            if(fBack.at(i) != '.'){
                availableLetter[albet.find(guess.at(i))] = true;       //set array slot corresponding to the letter to true
            }
        }

        feedback.push_back(fBack);         //add feedback to feedback vector
        guessNum++;                         //increments number of guesses

        if (guess==secretWord) {             // if guess is correct
            cout << "CORRECT!!! You guessed the secret word: " << secretWord << endl;
            return true;
        }
        else if(guessNum == MAX_GUESS_NUM){
            cout << "GAME OVER! all guesses have been made" << endl;    //game over
            cout << "the secret word was: " << secretWord << endl;
        }
    }
    return false;
}

void Wordle::print() {
    for(int i=0; i<guesses.size(); i++){        //loops through guesses, feedback vector
        cout << i+1 << ": " << guesses.at(i) << "\t" << feedback.at(i) << endl; //prints out guess and feedback for every made guess
    }
}

void Wordle::printAvailableLetters() {
    cout << "Available Letters:" << endl;
    for(int i=0; i<26; i++){                    //loops through alphabet/available letter array
        if(availableLetter[i]){                 //if letter is available
            cout << albet.at(i) << " ";         //print out letter
        }
    }
    cout << endl;
}
