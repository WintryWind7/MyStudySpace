package util;

import java.io.InputStream;
import java.sql.*;
import java.util.Properties;

public class DatabaseHelper {
	private static String username, password, url, driverClassName;
	
	static {
		Properties properties = new Properties();
		try {
			InputStream input = DatabaseHelper.class.getClassLoader().getResourceAsStream("database.properties");
			properties.load(input);
			username = properties.getProperty("username");
			password = properties.getProperty("password");
			url = properties.getProperty("url");
			driverClassName = properties.getProperty("driverClassName");
			Class.forName(driverClassName);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("Failed to load database configuration", e);
		}
	}

	public static Connection getConnection() {
		Connection conn = null;
		try {
			conn = DriverManager.getConnection(url, username, password);
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
		return conn;
	}

	public static void close(ResultSet rs, Statement st, Connection conn) {
		try {
			if (rs != null)
				rs.close();
			if (st != null)
				st.close();
			if (conn != null)
				conn.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
}
