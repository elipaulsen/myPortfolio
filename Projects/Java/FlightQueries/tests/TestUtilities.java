import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;
import org.junit.Assert;

import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class TestUtilities {
    // checks to see that the student Iterable has all the elements in the given set,
    // as well as no duplicates
    public static void checkUnordered(Set<String> expected, Iterable<String> student) {
        List<String> resultsAsList = new LinkedList();
        student.forEach(resultsAsList::add);
        Assert.assertEquals(expected.size(), resultsAsList.size());
        Set<String> resultsAsSet = new TreeSet(resultsAsList);
        Assert.assertEquals(expected, resultsAsSet);
    }

    public static Set<String> getExpectedResults1Col(String filename) throws IOException {
        Set<String> expected = new TreeSet<>();
        for (CSVRecord r : CSVFormat.EXCEL.parse(new FileReader(filename))) {
            expected.add(r.get(0));
        }
        return expected;
    }

    public static Set<String> getExpectedResults2Col(String filename) throws IOException {
        Set<String> expected = new TreeSet<>();
        for (CSVRecord r : CSVFormat.EXCEL.parse(new FileReader(filename))) {
            expected.add(r.get(0) + "," + r.get(1));
        }
        return expected;
    }
}
