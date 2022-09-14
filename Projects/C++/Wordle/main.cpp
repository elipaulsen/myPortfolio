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

    //MILESTONE 1 Unit Test Cases
    Wordle milestone1a("hotdog.csv");
    milestone1a.loadWordList();             //attempts to load hotdog.csv
    cout << milestone1a.getFile() << endl;
    milestone1a.printWordList();

    Wordle milestone1b("wordList.txt");     //loads real word file
    milestone1b.loadWordList();
    //milestone1b.printWordList();



    //MILESTONE 2 Unit Test Cases
    Wordle milestone2("wordList.txt");               //make wordle object with wordlist.txt as filename
    milestone2.loadWordList();                           //loads and reads wordList.txt
    milestone2.setRandomSecretWord();                    //sets a random word as the secret word
    cout << milestone2.getSecretWord() << endl;          //prints out secret word
    milestone2.setSecretWord("heart");               //sets word as a word that is in wordList.txt
    milestone2.setSecretWord("jaguar");             //sets word as a word not in wordList.txt
    cout << endl << milestone2.getSecretWord() << endl;           //prints out secret word



    //MILESTONE 3 Unit Test Cases
    Wordle milstone3("wordList.txt");
    milstone3.loadWordList();                       //loads wordList.txt
    milstone3.setSecretWord("sandwich");    //secret word cant be set to sandwich
    milstone3.setSecretWord("darts");       //secret word is darts
    cout << "Setting secret word to \"darts\". The secret word is " << milstone3.getSecretWord() << ".\n" << endl;
    milstone3.makeGuess("blue");        //guess does not count cause it was invalid
    milstone3.makeGuess("merry");
    milstone3.print();
    milstone3.makeGuess("rapid");
    milstone3.makeGuess("token");
    milstone3.makeGuess("other");
    milstone3.makeGuess("guard");
    milstone3.print();
    milstone3.makeGuess("darts");           //guessed secret word
    milstone3.print();
    cout << endl;




    //Milestone 5 Unit test cases
    Wordle milestone5("wordList.txt");
    milestone5.loadWordList();
    milestone5.setSecretWord("valid");      //secret word is valid
    milestone5.makeGuess("crest");          //.....
    milestone5.makeGuess("lavas");          //+!+..
    milestone5.makeGuess("valid");          //guessed correct word
    milestone5.print();
    cout << endl;

    //Milestone 6 Unit test cases
    Wordle milestone6("wordList.txt");
    milestone6.loadWordList();
    milestone6.setSecretWord("salet");
    milestone6.makeGuess("choir");
    milestone6.printAvailableLetters();
    milestone6.makeGuess("munch");
    milestone6.printAvailableLetters();
    cout << endl;



    //Wordle Game / Milestone 4
    Wordle game("wordList.txt");
    game.loadWordList();          //loads in wordList.txt
    //game.setRandomSecretWord();      // sets random word
    game.setSecretWord("crazy");          //secret word is crazy

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
