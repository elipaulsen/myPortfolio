import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;

public class Test {

    public static void main(String[] args) throws IOException, URISyntaxException {
        List<String> words = Files.readAllLines(Paths.get(Test.class.getResource("words (1).txt").toURI()));



        //for(int i = 1; i<100; i++) {
        Set<Nugget> s = new NuggetSet<>(21);
        for (String w : words)
            s.add(new Nugget(w));

        ((NuggetSet<Nugget>) s).debug();
           // ((NuggetSet<Nugget>) s).analyze();
        }


    }

