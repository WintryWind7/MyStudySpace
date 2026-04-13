<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>JSP 测试页面</title>
</head>
<body>
    <h1>你好，JSP！</h1>
    <p>当前时间：<%= new java.util.Date() %></p>

    <%
        // JSP脚本示例
        String name = request.getParameter("name");
        if (name != null) {
    %>
        <p>欢迎你，<%= name %>！</p>
    <%
        } else {
    %>
        <p>在URL后加 ?name=你的名字 来测试</p>
    <%
        }
    %>
</body>
</html>