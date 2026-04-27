<%@ page language="java" import="java.sql.*" pageEncoding="UTF-8"%>
<%@ page import="dao.ScoreDao"%>

<html>
<body>
<%
    request.setCharacterEncoding("UTF-8");
    String courseno = request.getParameter("courseno");
    String[] type = request.getParameterValues("type");
    String[] stuno = request.getParameterValues("stuno");
    String[] score = request.getParameterValues("score");
    ScoreDao sdao = new ScoreDao();
    if(score != null && score.length > 0) {
        sdao.updateScores(courseno, type, stuno, score);
    }
%>
<jsp:forward page="scoreForm.jsp"></jsp:forward>
</body>
</html>
