import java.util.Scanner;

public class Driver {

    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        Generator generator = new Generator(keyboard);
        generator.mainLoop();
        keyboard.close();
    }
}
