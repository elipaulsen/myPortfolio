import java.io.IOException;
import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;
import java.util.concurrent.atomic.AtomicInteger;

public class Query5 {
    public static String Query5(Iterable<FlightRecord> input) {
        Map<Integer,Integer> flights = new TreeMap<>();
        int maxFlights = -1;

        for (FlightRecord f : input) {
            if(flights.containsKey(f.MONTH)){
                flights.replace(f.MONTH,flights.get(f.MONTH)+1);
            }
            else{
                flights.put(f.MONTH,1);
            }
        }
        maxFlights = Collections.max(flights.values());

        return getKey(flights,maxFlights)+" had "+maxFlights+" flights";

    }
    public static <K, V> K getKey(Map<K, V> map, V value)
    {
        for (Map.Entry<K, V> entry: map.entrySet())
        {
            if (value.equals(entry.getValue())) {
                return entry.getKey();
            }
        }
        return null;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
        String r = Query5(input);
        System.out.println(r);
    }
}
