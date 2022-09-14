import java.io.IOException;
import java.util.*;

public class Query3 {

    public static int Query3(Iterable<FlightRecord> input) {
        Set<String> destinations = new HashSet<>();
        for (FlightRecord f : input) {
            if (f.ORIGIN.equals("CID")) {
                destinations.add(f.DEST);
            }
        }
        return destinations.size();
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights2019.csv");
        int results = Query3(input);
        System.out.println(results);
    }
}
