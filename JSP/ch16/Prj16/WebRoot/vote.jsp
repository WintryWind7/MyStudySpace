<%@ page language="java" import="java.sql.*" pageEncoding="gb2312"%>
<%@ include file="db.inc" %>
<html>
  <body>
   <%
   		String teacherno = request.getParameter("teacherno");
   		HttpSession sess = request.getSession();

   		if(sess.getAttribute("voted") != null) {
   	%>
   		<script>alert("666666"); location.href="display.jsp";</script>
   	<%
		sess.setAttribute("voted", null);
   		} else {
   			Connection conn = getConnection();
			String sql =
"UPDATE T_VOTE SET VOTE=VOTE+1 WHERE TEACHERNO=?";
			PreparedStatement ps = conn.prepareStatement(sql);
			ps.setString(1,teacherno);
			ps.executeUpdate();
			ps.close();
			conn.close();
	
			sess.setAttribute("voted", "true");
   	%>
		<jsp:forward page="display.jsp"></jsp:forward>
	<%
   		}
	%>
  </body>
</html>