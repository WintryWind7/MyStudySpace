<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.sql.*" %>
<html>
<head><title>学生查询</title></head>
<body>
<h2>学生信息查询</h2>
<form method="post">
姓名：<input type="text" name="name">
<input type="submit" value="查询">
</form>
<hr>
<%
    String name = request.getParameter("name");
    if (name != null && !name.trim().isEmpty()) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/student_db?useSSL=false&serverTimezone=UTC&characterEncoding=UTF-8",
                "root", "123456");
            ps = conn.prepareStatement("SELECT * FROM student WHERE name LIKE ?");
            ps.setString(1, "%" + name + "%");
            rs = ps.executeQuery();
%>
<table border="1">
<tr><th>学号</th><th>姓名</th><th>性别</th><th>年龄</th><th>专业</th><th>班级</th></tr>
<%
            while (rs.next()) {
%>
<tr>
<td><%= rs.getString("student_no") %></td>
<td><%= rs.getString("name") %></td>
<td><%= rs.getString("gender") %></td>
<td><%= rs.getInt("age") %></td>
<td><%= rs.getString("major") %></td>
<td><%= rs.getString("class_name") %></td>
</tr>
<%
            }
        } catch (Exception e) {
            out.print("错误：" + e.getMessage());
        } finally {
            if (rs != null) rs.close();
            if (ps != null) ps.close();
            if (conn != null) conn.close();
        }
    }
%>
</table>
</body>
</html>