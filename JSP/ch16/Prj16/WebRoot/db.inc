<%@ page language="java" import="java.sql.*" pageEncoding="gb2312"%>
<%!
	public Connection getConnection() throws Exception{
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection(
			"jdbc:mysql://localhost:3306/student?useSSL=false&serverTimezone=UTC&characterEncoding=gb2312",
			"root",
			"123456"
		);
		return conn;
	}
%>
