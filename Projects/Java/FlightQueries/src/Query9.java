import java.io.IOException;
import java.util.*;

public class Query9 {
    /*
    For each state, what is the airline (UNIQUE_CARRIER_NAME) with the most flights into that state?
     Return each result as STATE,AIRLINE.
     For example, if the airline most flying to Kentucky is
    United Parcel Service, then “KY,United Parcel Service”.
     */

    public static Iterable<String> Query9(Iterable<FlightRecord> input) {
        Map<String,Map<String,Integer>> map = new HashMap<>();
        List<String> result = new LinkedList<>();

        for(FlightRecord f : input){
            Map<String,Integer> innerMap = new HashMap<>();
            if(!map.containsKey(f.DEST_STATE_ABR)){
                innerMap.put(f.UNIQUE_CARRIER_NAME,1);
                map.put(f.DEST_STATE_ABR, innerMap);
            }
            else {
                innerMap = map.get(f.DEST_STATE_ABR);
                if(!innerMap.containsKey(f.UNIQUE_CARRIER_NAME)){
                    innerMap.put(f.UNIQUE_CARRIER_NAME,1);
                }
                else{
                    innerMap.replace(f.UNIQUE_CARRIER_NAME,innerMap.get(f.UNIQUE_CARRIER_NAME)+1);
                }
                map.replace(f.DEST_STATE_ABR, innerMap);
            }
        }
        map.forEach((key, value) -> {
            result.add(key+","+getKey(value,Collections.max(value.values())));
        });
        return result;
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
        Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
        Iterable<String> rs = Query9(input);
        for (String r : rs) {
            System.out.println(r);
        }
    }
}
