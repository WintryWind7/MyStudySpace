package homework13;

import java.sql.*;
import java.util.Scanner;

public class Demo11 {
    private static final String URL = "jdbc:mysql://localhost:3306/student?useSSL=false&serverTimezone=UTC";
    private static final String USER = "root";
    private static final String PASSWORD = "123456";

    public static void main(String[] args) {
        createDatabaseAndTable();

        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入学号:");
        String stuID = scanner.nextLine();
        System.out.print("请输入姓名:");
        String stuName = scanner.nextLine();

        addStudent(stuID, stuName);

        scanner.close();
    }

    private static void createDatabaseAndTable() {
        Connection conn = null;
        Statement stmt = null;

        try {
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306?useSSL=false&serverTimezone=UTC", USER, PASSWORD);
            stmt = conn.createStatement();

            String createDB = "CREATE DATABASE IF NOT EXISTS student";
            stmt.executeUpdate(createDB);

            stmt.executeUpdate("USE student");

            String createTable = "CREATE TABLE IF NOT EXISTS studentInfo (" +
                    "stuID VARCHAR(20) PRIMARY KEY," +
                    "stuName VARCHAR(50) NOT NULL" +
                    ")";
            stmt.executeUpdate(createTable);

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    private static void addStudent(String stuID, String stuName) {
        Connection conn = null;
        PreparedStatement pstmt = null;

        try {
            conn = DriverManager.getConnection(URL, USER, PASSWORD);
            String sql = "INSERT INTO studentInfo (stuID, stuName) VALUES (?, ?)";
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, stuID);
            pstmt.setString(2, stuName);

            return ;

        } catch (SQLException e) {
            e.printStackTrace();
            return ;
        } finally {
            try {
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
