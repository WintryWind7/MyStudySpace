<%@ page language="java" import="java.util.*" pageEncoding="UTF-8" %>
<%@ page import="dao.VoteDao" %>
<%@ page import="vo.Vote" %>
<html>
<body>
<form action="vote.jsp" method="post">
<table align="center">
    <caption>欢迎给教师投票<input type="submit" value="提交投票"></caption>
    <tr bgcolor="yellow">
        <td>编号</td>
        <td>姓名</td>
        <td>得票数</td>
        <td>投票</td>
    </tr>
    <%
        VoteDao vdao = new VoteDao();
        ArrayList<Vote> votes = vdao.getAllVotes();
        for(int i = 0; i < votes.size(); i++) {
            Vote vote = votes.get(i);
    %>
    <tr bgcolor="pink">
        <td><%= vote.getTeacherno() %></td>
        <td><%= vote.getTeachername() %></td>
        <td><img src="img/bar.jpg" width="<%= vote.getVotenumber() %>" height="10">
        <%= vote.getVotenumber() %></td>
        <td><input name="teacherno" type="checkbox" value="<%= vote.getTeacherno() %>">
        </td>
    </tr>
    <%
        }
    %>
</table>
</form>
</body>
</html>