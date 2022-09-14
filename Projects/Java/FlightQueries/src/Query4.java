import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;


/*
How many flights out of Cedar Rapids (CID) were there for each destination? You only need to
include destinations for which there was at least 1 flight from CID. Return each result as a String
with the format DEST=number of flights. For example, if there were 10 flights from CID to LAX,
then “LAX=10”.
 */
public class Query4 {

    public static Iterable<String> Query4(Iterable<FlightRecord> input) {
        Map<String,Integer> flights = new TreeMap<>();
        List<String> result = new LinkedList<>();

        for (FlightRecord f : input) {
            if (f.ORIGIN.equals("CID")) {
                if(flights.containsKey(f.DEST)){
                    flights.replace(f.DEST,flights.get(f.DEST)+1);
                }
                else{
                    flights.put(f.DEST,1);
                }
            }
        }
        flights.forEach((key, value) -> {
            result.add(key+"="+value);
        });

        return result;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
        Iterable<String> results = Query4(input);
        for (String s : results) {
            System.out.println(s);
        }
    }
}
