import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Date;

public class School {
    private Statement s;
    private Connection con;
    public School() throws SQLException {
        this.con = DriverManager.getConnection("jdbc:h2:/Users/elipaulsen/data");
        this.s = con.createStatement();
    }

    public void enrollStudent(String fName, String lName, int gradYear, String major) throws SQLException {
        s.execute(String.format("insert into students values('%s','%s',%s,'%s')",fName,lName,gradYear,major));
    }
}
