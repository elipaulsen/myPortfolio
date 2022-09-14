import java.io.IOException;
import java.text.DecimalFormat;
import java.util.*;

public class Query8 {

    public static Iterable<String> Query8(Iterable<FlightRecord> input) {
        Map<String,Float> totalFlights = new HashMap<>();
        Map<String,Float> inStateFlights = new HashMap<>();
        List<String> percents = new LinkedList<>();

        for (FlightRecord f : input) {
            if(!totalFlights.containsKey(f.ORIGIN_STATE_ABR)){
                if(f.ORIGIN_STATE_ABR.equals(f.DEST_STATE_ABR)){
                    inStateFlights.put(f.ORIGIN_STATE_ABR,1F);
                }
                else{
                    inStateFlights.put(f.ORIGIN_STATE_ABR,0F);
                }
                totalFlights.put(f.ORIGIN_STATE_ABR,1F);
            }
            else{
                if(f.ORIGIN_STATE_ABR.equals(f.DEST_STATE_ABR)){
                    inStateFlights.replace(f.ORIGIN_STATE_ABR,inStateFlights.get(f.ORIGIN_STATE_ABR)+1);
                }
                totalFlights.replace(f.ORIGIN_STATE_ABR,totalFlights.get(f.ORIGIN_STATE_ABR)+1);
            }
        }
        totalFlights.forEach((key, value) -> {
            float decimal = inStateFlights.get(key)/value;
            DecimalFormat df = new DecimalFormat("#.000");
            String withThreeDigits = df.format(decimal);
            if(decimal != 0){
                percents.add(key+"="+withThreeDigits);
            }
        });
        return percents;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
        Iterable<String> rs = Query8(input);
        for (String r : rs) {
            System.out.println(r);
        }
    }
}
