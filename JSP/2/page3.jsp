<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head><title>计算结果</title></head>
<body>
<h2>计算结果</h2>
<%
    String priceStr = "";
    Cookie[] cookies = request.getCookies();
    if (cookies != null) {
        for (Cookie c : cookies) {
            if ("price".equals(c.getName())) {
                priceStr = c.getValue();
                break;
            }
        }
    }

    String rateStr = request.getParameter("rate");

    Cookie rc = new Cookie("rate", rateStr);
    rc.setMaxAge(3600);
    response.addCookie(rc);

    try {
        double price = Double.parseDouble(priceStr);
        double rate = Double.parseDouble(rateStr);
        double result = price / rate;
%>
<p>图书价格：<%= priceStr %></p>
<p>汇率：<%= rateStr %></p>
<p>价格 / 汇率 = <b><%= String.format("%.2f", result) %></b></p>
<%
    } catch (NumberFormatException e) {
%>
<%
    }
%>
<a href="page1.jsp">返回重新输入</a>
</body>
</html>
