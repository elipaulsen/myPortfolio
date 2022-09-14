import java.io.IOException;
import java.util.*;

public class Query7 {
    public static Iterable<String> Query7(Iterable<FlightRecord> input) {
        Set<String> states = new HashSet<>();
        Set<String> possible = new HashSet<>();

        for (FlightRecord f : input){
            states.add(f.DEST_STATE_ABR);
            if(f.ORIGIN_STATE_ABR.equals("IA")){
                possible.add(f.DEST_STATE_ABR);
            }
        }
        states.removeAll(possible);
        return states;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
        Iterable<String> rs = Query7(input);
        for (String r : rs) {
            System.out.println(r);
        }
    }
}
