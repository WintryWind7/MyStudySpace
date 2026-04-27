<%@ page language="java" import="java.sql.*" pageEncoding="UTF-8" %>
<%@ page import="dao.VoteDao" %>
<html>
<body>
<%
    HttpSession sess = request.getSession();
    if (sess.getAttribute("voted") != null) {
        out.println("<script>alert('您已经投过票了！');location='display.jsp';</script>");
        return;
    }
    String[] teacherno = request.getParameterValues("teacherno");
    VoteDao vdao = new VoteDao();
    vdao.updateVotes(teacherno);
    sess.setAttribute("voted", "true");
%>

<jsp:forward page="display.jsp"></jsp:forward>
</body>
</html>