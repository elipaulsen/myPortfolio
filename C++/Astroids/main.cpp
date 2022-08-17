///////////////////////////////////////////////////////////////////
//
// Programmer: Eli Paulsen
// Date: April 27, 2022
// Description: Asteroids game:
//
///////////////////////////////////////////////////////////////////



#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include <time.h>
#include <list>
#include <cmath>
#include <iostream>

using namespace sf;

const int W = 1200;
const int H = 800;

float DEGTORAD = 0.017453f;

class Animation     //Animation Class
{
public:
	float Frame, speed;
	Sprite sprite;
    std::vector<IntRect> frames;

	Animation(){}

    Animation (Texture &t, int x, int y, int w, int h, int count, float Speed)      //Animation constructor
	{
	    Frame = 0;
        speed = Speed;

		for (int i=0;i<count;i++)
         frames.push_back( IntRect(x+i*w, y, w, h)  );

		sprite.setTexture(t);
		sprite.setOrigin(w/2,h/2);
        sprite.setTextureRect(frames[0]);
	}


	void update()       //update method
	{
    	Frame += speed;
		int n = frames.size();
		if (Frame >= n) Frame -= n;
		if (n>0) sprite.setTextureRect( frames[int(Frame)] );
	}

	bool isEnd()         //isEnd method
	{
	  return Frame+speed>=frames.size();
	}

};


class Entity        //Entity class/interface
{
public:
float x,y,dx,dy,R,angle;
bool life;
std::string name;
Animation anim;

Entity()
{
  life=1;
}

void settings(Animation &a,int X,int Y,float Angle=0,int radius=1)  //settings method
{
  anim = a;
  x=X; y=Y;
  angle = Angle;
  R = radius;
}

virtual void update(){};

void draw(RenderWindow &app)
{
  anim.sprite.setPosition(x,y);
  anim.sprite.setRotation(angle+90);

  app.draw(anim.sprite);

  CircleShape circle(R);
  circle.setFillColor(Color(255,0,0,170));
  circle.setPosition(x,y);
  circle.setOrigin(R,R);
  //app.draw(circle);

}

virtual ~Entity(){};
};


class asteroid: public Entity   //Asteroid class that implements Entity
{
public:
    static int numAsteroids;        //static member variable to keep track of number of asteroids
    asteroid()
    {
        //random speed
        dx=rand()%8-4;
        dy=rand()%8-4;
        name="asteroid";
        numAsteroids++;
    }


    void  update()
      {
       x+=dx;       //updates coordinates
       y+=dy;

       if (x>W) x=0;
       if (x<0) x=W;
       if (y>H) y=0;
       if (y<0) y=H;
      }
    ~asteroid() {
        numAsteroids--;     //decrements asteroids when deleted
    }



};



class bullet: public Entity
{
public:
  bullet()
  {
    name="bullet";
  }

void  update()
  {
   dx=cos(angle*DEGTORAD)*6;
   dy=sin(angle*DEGTORAD)*6;
  // angle+=rand()%6-3;
   x+=dx;
   y+=dy;

   if (x>W || x<0 || y>H || y<0) life=0;
  }

};


class player: public Entity     //Player Class that implements Entity
{
public:
   bool thrust;

   player()
   {
     name="player";
   }

   void update()        //update method that will update location of all entities
   {
     if (thrust)
      { dx+=cos(angle*DEGTORAD)*0.2;
        dy+=sin(angle*DEGTORAD)*0.2; }
     else
      { dx*=0.99;
        dy*=0.99; }

    int maxSpeed=15;
    float speed = sqrt(dx*dx+dy*dy);
    if (speed>maxSpeed)
     { dx *= maxSpeed/speed;
       dy *= maxSpeed/speed; }

    x+=dx;
    y+=dy;

    //wraps around screen

    if (x>W) x=0;
    if (x<0) x=W;
    if (y>H) y=0;
    if (y<0) y=H;
   }

};

class UFO: public Entity{       //UFO class that implements entity
public:

    UFO(){
        x = 50;
        y = rand() % H;
        dx = 3; //speed is 3
        dy = 0;
        name = "ufo";
    }


    void update() {
        x += dx;        //move right each frame
        if(x > W){
            x = 0;          //ufo will wrap around screen if not killed
        }
    }
};




bool isCollide(Entity *a,Entity *b)     //isCollide method that returns true if two entity objects touch each-other
{
  return (b->x - a->x)*(b->x - a->x)+
         (b->y - a->y)*(b->y - a->y)<
         (a->R + b->R)*(a->R + b->R);
}


int asteroid::numAsteroids{0};

int main()
{
    srand(time(0));     //seeding rng


    RenderWindow app(VideoMode(W, H), "Asteroids!");    //renders window
    app.setFramerateLimit(60);

    //Loads in images
    Texture t1,t2,t3,t4,t5,t6,t7,t8;
    t1.loadFromFile("images/spaceship.png");
    t2.loadFromFile("images/background.jpg");
    t3.loadFromFile("images/explosions/type_C.png");
    t4.loadFromFile("images/rock.png");
    t5.loadFromFile("images/fire_blue.png");
    t6.loadFromFile("images/rock_small.png");
    t7.loadFromFile("images/explosions/type_B.png");
    t8.loadFromFile("images/ufo1.png");          // attributed to Adib Sulthan Flaticon.com

    t1.setSmooth(true);
    t2.setSmooth(true);
    t8.setSmooth(true);


    Sprite background(t2);

    //loads animations
    Animation sExplosion(t3, 0,0,256,256, 48, 0.5);
    Animation sRock(t4, 0,0,64,64, 16, 0.2);
    Animation sRock_small(t6, 0,0,64,64, 16, 0.2);
    Animation sBullet(t5, 0,0,32,64, 16, 0.8);
    Animation sPlayer(t1, 40,0,40,40, 1, 0);
    Animation sPlayer_go(t1, 40,40,40,40, 1, 0);
    Animation sExplosion_ship(t7, 0,0,192,192, 64, 0.5);
    Animation ufo(t8,0,0,512,512,1,0);


    ufo.sprite.scale(0.15,0.15);

    //loads in font
   Font font;
    if (!font.loadFromFile("images/RockoFLF.ttf"))
    {
        return EXIT_FAILURE;
    }


    //creats score text
    Text text;
    text.setFont(font);
    text.setFillColor(Color::White);
    text.setCharacterSize(50);

    //creates game over text
    Text gameOver;
    gameOver.setFont(font);
    gameOver.setFillColor(Color::Red);
    gameOver.setCharacterSize(100);

    //creates main menu text
    Text menu;
    menu.setFont(font);
    menu.setFillColor(Color::Green);
    menu.setCharacterSize(80);

    //loads explosion sound
    SoundBuffer explosion;
    if (!explosion.loadFromFile("images/explode.ogg")){      //loads in an explosion sound
        return EXIT_FAILURE;
    }

    Sound explode;
    explode.setBuffer(explosion);

    //loads laser sound
    SoundBuffer lasr;
    if (!lasr.loadFromFile("images/laser.ogg")){      //loads in an explosion sound
        return EXIT_FAILURE;
    }

    Sound laser;
    laser.setBuffer(lasr);

    //loads in ufo music
    Music sound;
    sound.openFromFile("images/ufoSound.ogg");
    bool musicPlaying = false;
    sound.setLoop(true);


    //creates list of entities
    std::list<Entity*> entities;

    //creates 15 new asteroids
    for(int i=0;i<15;i++)
    {
      asteroid *a = new asteroid();
      a->settings(sRock, rand()%W, rand()%H, rand()%360, 25);
      entities.push_back(a);
    }


    //creates one new player
    player *p = new player();
    p->settings(sPlayer,200,200,0,20);
    entities.push_back(p);



    int numUfo = 0;     //tracks number of ufos on screen
    int score = 0;       //tracks user score
    int userLives = 5;      //tracks user lives

    //game states
    bool mainMenu = true;
    bool inGame = false;
    bool dead = false;

    int diff = 1; //default difficulty is 1;

    /////main loop/////
    while (app.isOpen()) {
        //Main Menu
        if(mainMenu){
            app.clear();
            menu.setString("WELCOME TO ASTEROIDS\n Choose Difficulty!\nClassic: press C\nAdvanced: press A\nLegend: press L");
            app.draw(menu);
            Event event;
            while (app.pollEvent(event)) {
                if (event.type == Event::Closed) {
                    app.close();
                }

                if (event.type == Event::KeyPressed) {
                    // Difficulty Picker
                    if (event.key.code == Keyboard::C) {    //fires bullets when user hits space
                        diff = 1;
                        mainMenu = false;
                        inGame = true;
                    }
                    else if (event.key.code == Keyboard::A) {    //fires bullets when user hits space
                        diff = 3;
                        mainMenu = false;
                        inGame = true;
                    }
                    else if (event.key.code == Keyboard::L) {    //fires bullets when user hits space
                        diff = 10;
                        mainMenu = false;
                        inGame = true;
                    }

                }
            }
            //displays screen
            app.display();
        }
        //game loop
        if(inGame) {
            Event event;
            while (app.pollEvent(event)) {
                if (event.type == Event::Closed) {
                    app.close();
                }

                if (event.type == Event::KeyPressed) {
                    if (event.key.code == Keyboard::Space) {    //fires bullets when user hits space
                        bullet *b = new bullet();
                        b->settings(sBullet, p->x, p->y, p->angle, 10);
                        entities.push_back(b);      //adds bullets to entity list
                        laser.play();
                    }
                }
            }

            //Directional movement reader
            if (Keyboard::isKeyPressed(Keyboard::Right)) {
                p->angle += 3;
            }
            if (Keyboard::isKeyPressed(Keyboard::Left)) {
                p->angle -= 3;
            }
            if (Keyboard::isKeyPressed(Keyboard::Up)) {
                p->thrust = true;
            } else {
                p->thrust = false;
            }


            //checks for collisions and explosions
            for (auto a: entities) {
                for (auto b: entities) {
                    if (a->name == "asteroid" && b->name == "bullet")   //ASTEROID AND BULLET COLLISON
                        if (isCollide(a, b)) {
                            //schedules to delete a,b
                            a->life = false;
                            b->life = false;
                            explode.play(); //plays explode sound

                            score += 100;       //adds to score

                            //adds explosioon to entities
                            Entity *e = new Entity();
                            e->settings(sExplosion, a->x, a->y);
                            e->name = "explosion";
                            entities.push_back(e);


                            for (int i = 0; i < 2; i++) {
                                if (a->R == 15) continue;
                                Entity *e = new asteroid();
                                e->settings(sRock_small, a->x, a->y, rand() % 360, 15);
                                entities.push_back(e);
                            }

                        }

                    if (a->name == "player" && b->name == "asteroid") { //PLAYER AND ASTEROID COLLISION
                        if (isCollide(a, b)) {
                            //schedules to delete b
                            b->life = false;
                            explode.play(); //play explode sound
                            userLives--;    //lose a life


                            Entity *e = new Entity();
                            e->settings(sExplosion_ship, a->x, a->y);
                            e->name = "explosion";
                            entities.push_back(e);

                            p->settings(sPlayer, W / 2, H / 2, 0, 20);
                            p->dx = 0;
                            p->dy = 0;
                        }
                    }
                    if (a->name == "player" && b->name == "ufo") {//PLAYER AND UFO COLLISON
                        if (isCollide(a, b)) {
                            b->life = false;
                            numUfo--;
                            userLives--;


                            Entity *e = new Entity();
                            e->settings(sExplosion_ship, b->x, b->y);
                            e->name = "explosion";
                            entities.push_back(e);

                            p->settings(sPlayer, W / 2, H / 2, 0, 20);
                            p->dx = 0;
                            p->dy = 0;
                        }
                    }
                    if (a->name == "bullet" && b->name == "ufo") { //BULLET AND UFO COLLISON
                        if (isCollide(a, b)) {
                            b->life = false;
                            a->life = false;
                            numUfo--;
                            explode.play();

                            score += 500;

                            Entity *e = new Entity();
                            e->settings(sExplosion_ship, b->x, b->y);
                            e->name = "explosion";
                            entities.push_back(e);


                        }
                    }
                    if (a->name == "asteroid" && b->name == "ufo") {    //UFO AND ASTEROID COLLISION
                        if (isCollide(a, b)) {
                            a->life = false;
                            explode.play();

                            Entity *e = new Entity();
                            e->settings(sExplosion_ship, b->x, b->y);
                            e->name = "explosion";
                            entities.push_back(e);
                        }
                    }
                }
            }

            if (p->thrust) {
                p->anim = sPlayer_go;
            } else {
                p->anim = sPlayer;
            }

            //entity goes away if exploded
            for (auto e: entities) {
                if (e->name == "explosion") {       //PLAYS EXPLOSION ANIMATIONS
                    if (e->anim.isEnd()) {
                        e->life = 0;
                    }
                }
            }
            /*
            //creates new astroids and fires them into screen randomly
            if (rand()%150==0)
             {
               asteroid *a = new asteroid();
               a->settings(sRock, 0,rand()%H, rand()%360, 25);
               entities.push_back(a);
             }
             */

            if (numUfo != 0 && !musicPlaying) { //PLAYS UFO MUSIC
                sound.play();
                musicPlaying = true;
            }
            //creates new ufo randomly
            if (numUfo < diff && rand() % 350/diff == 1) {
                UFO *u = new UFO();
                u->settings(ufo, 0, rand() % H, -90, 16);
                entities.push_back(u);
                numUfo++;
                musicPlaying = false;
            }

            if(asteroid::numAsteroids == 0){    //CREATES 15 NEW ASTEROID WHEN ALL OG ARE GONE
                //creates 15 new asteroids
                for(int i=0;i<15;i++)
                {
                    asteroid *a = new asteroid();
                    a->settings(sRock, rand()%W, rand()%H, rand()%360, 25);
                    entities.push_back(a);
                }
            }


            for (auto i = entities.begin(); i != entities.end();) {
                Entity *e = *i;

                e->update();    //UPDATES ALL ENTITY OBJECTS
                e->anim.update();

                //if entity dies then entity will be deleted
                if (e->life == false) {
                    i = entities.erase(i);
                    if (e->name == "ufo") {
                        musicPlaying = false;
                        sound.stop();
                    }
                    delete e;
                } else {
                    i++;
                }
            }

            text.setString(std::to_string(score) + "\t\t\t\t\t\t\t\t" + std::to_string(userLives) + " lives left");

            //////draw//////

            app.draw(background);

            for (auto i: entities) {
                i->draw(app);
            }
            app.draw(text);

            app.display();   //displays every frame in main loop

            if(userLives <= 0){ //ENDS GAME IF LIVES RUN OUT
                dead = true;
                inGame = false;
                sound.stop();
                musicPlaying = false;
            }
        }
        if(dead){//GAME OVER LOOP
            app.clear();
            Event event;
            while (app.pollEvent(event)) {
                if (event.type == Event::Closed) {
                    app.close();
                }

                if (event.type == Event::KeyPressed) {
                    if (event.key.code == Keyboard::R) {    //fires bullets when user hits space
                        dead = false;
                        inGame = true;
                        userLives = 5;
                        score = 0;
                    }
                }
            }
            gameOver.setString("GAME OVER\nYOU SCORED: "+std::to_string(score)+"\nPress R to restart game");

            app.draw(gameOver);
            app.display();      //DISPLAYS
        }
    }


    return 0;
}
