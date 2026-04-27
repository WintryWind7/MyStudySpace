<%@ page language="java" import="java.util.*" pageEncoding="UTF-8" %>
<%@ page import="dao.ScoreDao" %>
<%@ page import="vo.Score" %>

<html>
<body>
    <div align="center">
    <%
    String courseno = request.getParameter("courseno");
    if(courseno == null) courseno = "001";
    %>
    <form>
        选择课程编号：
        <select name="courseno" onchange="this.form.submit()">
            <option value="001" <%= courseno.equals("001") ? "selected" : "" %>>001</option>
            <option value="002" <%= courseno.equals("002") ? "selected" : "" %>>002</option>
        </select>
    </form>
    输入课程编号为<%=courseno%>的所有学生成绩
    <form action="scoreUpdate.jsp" method="post">
    <input name="courseno" type="hidden" value="<%=courseno%>">
    <input type="submit" value="提交成绩">
    <table>
        <tr bgcolor="yellow">
            <td>学号</th>
            <td>姓名</th>
            <td>考试类型</th>
            <td>分数</th>
        </tr>
        <%
        ScoreDao sdao = new ScoreDao();
        ArrayList scores = sdao.getAllScoresByCourseNo(courseno);
        for(int i = 0; i < scores.size(); i++) {
            Score score = (Score)scores.get(i);
        %>
        <tr bgcolor="pink">
            <td><%= score.getStuno() %></th>
            <td><%= score.getStuname() %></th>
            <td><%= score.getType() %></th>
            <%
            if(score.getScorenumber() == null) {
            %>
                <input name="score" type="text" size="4">
                <input name="type" type="hidden" value="<%= score.getType() %>">
                <input name="stuno" type="hidden" value="<%= score.getStuno() %>">
            <% } else {
                out.print(score.getScorenumber());
            }
            %>
            </th>
        </tr>
        <%
        }
        %>
    </table>
    </form>
    </div>
</body>
</html>
