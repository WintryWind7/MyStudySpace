<%@ page language="java" import="java.sql.*" pageEncoding="gb2312"%>
<%@ include file="db.inc" %>
<html>
  <body>
  <table align="center">
  	<caption>欢迎给教师投票</caption>
   <tr bgcolor="yellow">
   	<td>编号</td>
   	<td>姓名</td>
   	<td>得票数</td>
   	<td>投票</td>
   </tr>
   <%
   		Connection conn = getConnection();
   		Statement stat = conn.createStatement();
		String sql = 
"SELECT TEACHERNO,TEACHERNAME,VOTE FROM T_VOTE";
		ResultSet rs = stat.executeQuery(sql);
		while(rs.next()){
			String teacherno = rs.getString("TEACHERNO");
			String teachername = rs.getString("TEACHERNAME");
			int vote = rs.getInt("VOTE");
	%>
		<tr bgcolor="pink">
   		<td><%=teacherno %></td>
   		<td><%=teachername %></td>
   		<td><img src="img/bar.jpg" width="<%=vote%>" height="10"> <%=vote%></td>
   		<td><a href="vote.jsp?teacherno=<%=teacherno%>">ͶƱ</a></td>
   		</tr>
	<%		
		}
		stat.close();
		conn.close();
	%>
   </table>
  </body>
</html>
