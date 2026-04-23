<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head><title>输入汇率</title></head>
<body>
<h2>请输入汇率</h2>
<%
    String price = request.getParameter("price");
    Cookie c = new Cookie("price", price);
    c.setMaxAge(3600);
    response.addCookie(c);
%>
<p>图书价格已记录：<%= price %></p>
<form action="page3.jsp" method="post">
    汇率：<input type="text" name="rate" required />
    <input type="submit" value="计算" />
</form>
</body>
</html>
