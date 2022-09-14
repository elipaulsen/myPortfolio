import java.io.IOException;
import java.util.*;

public class Query10 {

    public static Iterable<String> Query10(Iterable<FlightRecord> input) {
        Set<String> set = new HashSet<>();
        Set<String> result = new HashSet<>();

        for(FlightRecord i : input){
            if(i.ORIGIN.equals("CID")) {
                set.add(i.DEST);
            }
        }

        for(FlightRecord j : input){
            if(j.DEST.equals("LAX") && set.contains(j.ORIGIN)) {
                result.add("CID->"+j.ORIGIN+"->LAX");
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
        Timer t = new Timer();
        t.start();
        Iterable<String> results = Query10(input);
        t.end();
        for (String s : results) {
            System.out.println(s);
        }
        System.out.println(t.elapsedSeconds());
    }
}



