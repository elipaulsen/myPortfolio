import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;


public class Query6 {
    public static String Query6(Iterable<FlightRecord> input) {
        Map<String,Integer> flights = new HashMap<>();
        Integer maxFlights = 0;
        String statePair = "";


        for (FlightRecord f : input) {
            statePair = orderStates(f.ORIGIN_STATE_ABR,f.DEST_STATE_ABR);
            if(flights.containsKey(statePair)){
                flights.replace(statePair,flights.get(statePair)+1);
            }
            else{
                flights.put(statePair,1);
            }
            if(flights.get(statePair)> maxFlights){
                maxFlights = flights.get(statePair);
            }
        }
        return getKey(flights,maxFlights);
    }

    public static String orderStates(String s1, String s2){
        if(s1.compareTo(s2) < 0)  return s1+","+s2;
        return s2+","+s1;
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
        String r = Query6(input);
        System.out.println(r);
    }
}
