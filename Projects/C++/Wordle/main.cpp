///////////////////////////////////////////////////////////////////
//
// Programmer: Eli Paulsen
// Date: Feb 16, 2022
// Description: Replicate the word game WORDLE using c++ object
// oriented programming.
///////////////////////////////////////////////////////////////////

#include <iostream>
#include "Wordle.cpp"


using namespace std;

int main() {

    
    Wordle game("wordList.txt");
    game.loadWordList();          //loads in wordList.txt
    game.setRandomSecretWord();      // sets random word
   
    //game intro / Instructions
    cout << "Welcome to Wordle" << "\nYou have six tries to guess a five-letter english word." << endl
         << "press enter to submit your guess" << endl
         << "After each guess, you will get feedback to how close your guess was to the word. \n"
            "! is the correct letter in the correct spot. \n"
            "+ is the correct letter in the wrong spot. \n"
            ". is a letter that does not appear in the word. ";

    int i = 0;
    string tmpGuess;
    bool win = false;
    while(i < 6){
        cout << "enter guess: " << endl;
        cin >> tmpGuess;    //reads in users guess and stores it in temporary variable
        if(game.makeGuess(tmpGuess)){     //if guess is correct then end the loop and set win as true
            i = 6;
            win = true;
            break;
        }
        i = game.getGuessNum();   //set i = to the number of valid guesses user has made
        if(i != 6){
            game.print();         //prints feedback and guesses after each guess
            game.printAvailableLetters();       //prints available letters after every guess
        }
    }
    if(win){    //if user guesses word successfully
        game.print();
        cout << "WINNER: You guessed this wordle in " << game.getGuessNum() << " attempt(s)!" << endl;
    }
    else{       //if user fails to solve wordle
        game.print();
        cout << "You could not complete this wordle, better luck next time" << endl;
    }

}
