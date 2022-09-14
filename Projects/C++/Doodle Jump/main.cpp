///////////////////////////////////////////////////////////////////
//
// Programmer: Eli Paulsen
// Date: Mar 30, 2022
// Description: Doodle Jump sfml game
///////////////////////////////////////////////////////////////////

#include <SFML/Graphics.hpp>
#include <time.h>
#include <SFML/Audio.hpp>
#include "string"
#include "vector"

using namespace sf;

class point{
public:
    int getX() const;       //x getter method
    void setX(int newX);    //x setter method
    int getY() const;       //y getter method
    void setY(int newY);    //y setter method
private:
    int x;
    int y;
};

//point class methods:

int point::getX() const {
    return x;
}

int point::getY() const {
    return y;
}

void point::setX(int newX) {
    x = newX;
}

void point::setY(int newY) {
    y = newY;
}


int main()
{
    srand(time(0));

    RenderWindow app(VideoMode(400, 533), "Doodle Game!");      //creates window
    app.setFramerateLimit(60);      //sets max fps to 60

    SoundBuffer evilLaugh;
    if (!evilLaugh.loadFromFile("laugh.ogg")){      //loads in an evil laugh
        return EXIT_FAILURE;
    }

    Sound deathSound;
    deathSound.setBuffer(evilLaugh);


    Font font;
    if (!font.loadFromFile("RockoFLF.ttf"))
    {
        return EXIT_FAILURE;
    }

    //creats text
    Text text;
    text.setFont(font);
    text.setFillColor(Color::Black);
    text.setCharacterSize(50);

    //creats menu text
    Text menu;
    menu.setFont(font);
    menu.setFillColor(Color::Green);
    menu.setString("Doodle Jump\npress S to play\nuse L/R arrows\n to move\n horizontally\n and see how high\n you can jump");
    menu.setCharacterSize(48);

    //loads in textures used for doodle jump
    Texture t1,t2,t3;
    t1.loadFromFile("images/background.png");
    if (!t1.loadFromFile("images/background.png")) { return EXIT_FAILURE; }

    t2.loadFromFile("images/platform.png");
    if (!t2.loadFromFile("images/platform.png")) { return EXIT_FAILURE; }

    t3.loadFromFile("images/doodle.png");
    if (!t3.loadFromFile("images/doodle.png")) { return EXIT_FAILURE; }

    //initializes Sprites
    Sprite sBackground(t1), sPlat(t2), sPers(t3);

    //creates array to hold points called plat
    point plat[20];

    bool gameRestart = false;

    //sets each platform to be in a random position in window
    for (int i=0;i<10;i++)
      {
       plat[i].setX(rand()%400);
       plat[i].setY(rand()%533);
      }

    //game variables
	int x=100,y=100,h=200;
    float dx=0,dy=0;
    bool dead = false;
    bool mainMenu = true;
    int currScore = 0;
    int highScore = 0;
    float fallVelo;
    int jumpHeight;


    //main game loop
    while (app.isOpen()) {

        //checking for events
        Event e;
        while (app.pollEvent(e)) {

            if (e.type == Event::Closed) {
                app.close();        //close the window
            }


        }
        //FEATURE 1 : I added a main menu
        if(mainMenu){
            app.clear();
            app.draw(menu);
            app.display();
            while (app.pollEvent(e)){
                if(e.type == e.Closed){
                    app.close();
                }
                //FEATURE 2 : I added multiple difficulty that make it harder to control character
                if (Keyboard::isKeyPressed(Keyboard::S)) {//right
                    menu.setCharacterSize(40);
                    menu.setString("Choose Difficulty\n"
                                   "press C for Classic\n"
                                   "press A for Advanced\n"
                                   "press X for X-treme");
                }
                if (Keyboard::isKeyPressed(Keyboard::C)){
                    fallVelo = 0.2; //normal fall speed
                    jumpHeight = -10;   //normal jumpheight
                    mainMenu = false;
                }
                if (Keyboard::isKeyPressed(Keyboard::A)){
                    fallVelo = 0.4;     //you fall faster
                    jumpHeight = -14;   //but jump higher
                    mainMenu = false;
                }
                if (Keyboard::isKeyPressed(Keyboard::X)){
                    fallVelo = 1.2;     //you fall faster
                    jumpHeight = -25;       //but jump higher
                    mainMenu = false;       //gets out of main menu
                }

            }

        }
        else if(!dead){ //main game


            //resets the game after it has been played
            if (gameRestart){
                for (int i=0;i<10;i++)
                {
                    plat[i].setX(rand()%400);
                    plat[i].setY(rand()%533);
                }
                x=100,y=100,h=200;
                dx=0,dy=0;
                currScore = 0;
                highScore = 0;
                gameRestart = false;
            }

        //reads in input and moves character
        if (Keyboard::isKeyPressed(Keyboard::Right)) { x += 3; }      //right
        if (Keyboard::isKeyPressed(Keyboard::Left)) { x -= 3; }      //left



        dy += fallVelo;
        y += dy;


        if (y < h) {
            //remakes random points when character moves up the window
            for (int i = 0; i < 10; i++) {
                y = h;
                plat[i].setY(plat[i].getY() - dy);
                if (plat[i].getY() > 533) {
                    plat[i].setY(0);
                    plat[i].setX(rand() % 400);
                }
            }
        }

        for (int i = 0; i < 10; i++) {
            //if charcter hits a platform
            if ((x + 50 > plat[i].getX()) && (x + 20 < plat[i].getX() + 68) && (y + 70 > plat[i].getY()) &&
                (y + 70 < plat[i].getY() + 14) && (dy > 0)) {
                dy = jumpHeight;   //jump up
            }

            sPers.setPosition(x, y);    //sets position of character


            app.draw(sBackground);      //draws background
            app.draw(sPers);            //draws character
        }

        for (int i = 0; i < 10; i++) {
            sPlat.setPosition(plat[i].getX(), plat[i].getY());        //sets positions of platforms
            app.draw(sPlat);            //draws platforms
        }

        currScore -= dy;        //keeps track of score
        if (currScore < 0) {
            currScore = 0;          //score cant go negative
        }
        if(currScore>highScore){        //keeps highest score
            highScore=currScore;
        }
        text.setString(std::to_string(highScore));      //draws highscore in top left corner

        app.draw(text);

        if (y > 533) {          //when character fall off app's window
            dead = true;            //dead = true
            deathSound.play();      // plays death sound
        }


        app.display();      //displays
    }
        else if(dead){  //when dead


            app.clear();        //black screen
            text.setString("\t GAME OVER\n\n"   //game over message
                           "\n\npress R to restart\n\n\t\t\t"+std::to_string(highScore));
            text.setFillColor(Color::Red);
            app.draw(text);


            app.display();
            while (app.pollEvent(e)){
                if(e.type == e.Closed){
                    dead = false;
                    app.close();
                }
                //restart game button
                if (Keyboard::isKeyPressed(Keyboard::R)) {       //right
                    dead = false;
                    gameRestart = true;
                    text.setFillColor(Color::Black);
                    text.setString(std::to_string(currScore));
                }
            }
        }

}

    return 0;
}
