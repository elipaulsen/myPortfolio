import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;
import java.util.Set;
import java.util.HashSet;


public class QueryTest {
    @Test
    public void test0() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            int result = Query0.Query0(input);
            Assert.assertEquals(2, result);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            int result = Query0.Query0(input);
            Assert.assertEquals(5, result);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            int result = Query0.Query0(input);
            Assert.assertEquals(6, result);
        }
    }

    @Test
    public void test1() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            int total = Query1.Query1(input);
            Assert.assertEquals(275, total);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            int total = Query1.Query1(input);
            Assert.assertEquals(409, total);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            int total = Query1.Query1(input);
            Assert.assertEquals(444, total);
        }
    }

    @Test
    public void test2() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            Iterable<String> results = Query2.Query2(input);
            Set<String> expected = TestUtilities.getExpectedResults2Col("query2_2020.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            Iterable<String> results = Query2.Query2(input);
            Set<String> expected = TestUtilities.getExpectedResults2Col("query2_1990.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            Iterable<String> results = Query2.Query2(input);
            Set<String> expected = TestUtilities.getExpectedResults2Col("query2_2005.txt");
            TestUtilities.checkUnordered(expected, results);
        }
    }

    @Test
    public void test3() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            int result = Query3.Query3(input);
            Assert.assertEquals(57, result);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            int result = Query3.Query3(input);
            Assert.assertEquals(87, result);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            int result = Query3.Query3(input);
            Assert.assertEquals(63, result);
        }
    }

    @Test
    public void test4() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            Iterable<String> results = Query4.Query4(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query4_2020.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            Iterable<String> results = Query4.Query4(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query4_1990.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            Iterable<String> results = Query4.Query4(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query4_2005.txt");
            TestUtilities.checkUnordered(expected, results);
        }
    }

    @Test
    public void test5() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            String result = Query5.Query5(input);
            Assert.assertEquals("9 had 13832 flights", result);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            String result = Query5.Query5(input);
            Assert.assertEquals("6 had 23800 flights", result);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            String result = Query5.Query5(input);
            Assert.assertEquals("1 had 21945 flights", result);
        }
    }

    @Test
    public void test6() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            String result = Query6.Query6(input);
            Assert.assertEquals("CA,CA", result);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            String result = Query6.Query6(input);
            Assert.assertEquals("AK,AK", result);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            String result = Query6.Query6(input);
            Assert.assertEquals("AK,AK", result);
        }
    }

    @Test
    public void test7() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            Iterable<String> results = Query7.Query7(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query7_2020.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            Iterable<String> results = Query7.Query7(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query7_1990.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            Iterable<String> results = Query7.Query7(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query7_2005.txt");
            TestUtilities.checkUnordered(expected, results);
        }
    }

    @Test
    public void test8() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            Iterable<String> results = Query8.Query8(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query8_2020.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            Iterable<String> results = Query8.Query8(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query8_1990.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            Iterable<String> results = Query8.Query8(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query8_2005.txt");
            TestUtilities.checkUnordered(expected, results);
        }
    }

    @Test
    public void test9() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            Iterable<String> results = Query9.Query9(input);
            Set<String> expected = TestUtilities.getExpectedResults2Col("query9_2020.txt");
            try {
                TestUtilities.checkUnordered(expected, results);
            } catch (AssertionError e) {
                expected.remove("VI,American Airlines Inc.");
                expected.add("VI,Cape Air");
                TestUtilities.checkUnordered(expected, results);
            }
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            Iterable<String> results = Query9.Query9(input);
            Set<String> expected = TestUtilities.getExpectedResults2Col("query9_1990.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            Iterable<String> results = Query9.Query9(input);
            Set<String> expected = TestUtilities.getExpectedResults2Col("query9_2005.txt");
            try {
                TestUtilities.checkUnordered(expected, results);
            } catch (AssertionError e) {
                expected.remove("WA,Alaska Airlines Inc.");
                expected.add("WA,Southwest Airlines Co.");
                TestUtilities.checkUnordered(expected, results);
            }

        }
    }

    @Test
    public void test10() throws IOException {
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2020.csv");
            Iterable<String> results = Query10.Query10(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query10_2020.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights1990.csv");
            Iterable<String> results = Query10.Query10(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query10_1990.txt");
            TestUtilities.checkUnordered(expected, results);
        }
        {
            Iterable<FlightRecord> input = DataImporter.getData("flights2005.csv");
            Iterable<String> results = Query10.Query10(input);
            Set<String> expected = TestUtilities.getExpectedResults1Col("query10_2005.txt");
            TestUtilities.checkUnordered(expected, results);
        }
    }
}