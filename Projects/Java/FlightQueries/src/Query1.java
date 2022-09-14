import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Query1 {

    public static int Query1(Iterable<FlightRecord> input) {
        int sum = 0;
        for (FlightRecord r : input) {
            if (r.ORIGIN.equals("CID")) {
                sum++;
            }
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
        int total = Query1(input);
        System.out.println(total);
    }
}
