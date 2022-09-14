import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Query0 {

    public static int Query0(Iterable<FlightRecord> input) {
        int sum = 0;

        // There are two common methods of iterating over an Iterable

        // 1. Use the Iterator from the Iterable
        /*
        Iterator<FlightRecord> it = input.iterator();
        while(it.hasNext()) {
           FlightRecord r = it.next();
           if (r.ORIGIN.equals("LAX") && r.DEST.equals("ORD") && r.MONTH == 8) {
                sum++;
            }
        }
         */

        // 2. Use Java's "for each" syntax.
        // Read this as "for each FlightRecord r from input"
        for (FlightRecord r : input) {
            if (r.ORIGIN.equals("LAX") && r.DEST.equals("ORD") && r.MONTH == 8) {
                sum++;
            }
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
        int result = Query0(input);
        System.out.println(result);
    }
}
