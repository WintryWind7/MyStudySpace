package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import vo.Vote;

public class VoteDao {
    private Connection conn = null;

    public void initConnection() throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        String url = "jdbc:mysql://localhost:3306/student?useSSL=false&serverTimezone=UTC&characterEncoding=gb2312";
        conn = DriverManager.getConnection(url,"root","123456");
    }

    //返回所有教师及其得票数
    public ArrayList<Vote> getAllVotes() throws Exception {
        ArrayList<Vote> al = new ArrayList<Vote>();
        initConnection();
        String sql = "SELECT TEACHERNO,TEACHERNAME,VOTE FROM T_VOTE";
        Statement stat = conn.createStatement();
        ResultSet rs = stat.executeQuery(sql);
        while(rs.next()) {
            Vote vote = new Vote();
            vote.setTeacherno(rs.getString("TEACHERNO"));
            vote.setTeachername(rs.getString("TEACHERNAME"));
            vote.setVotenumber(rs.getInt("VOTE"));
            al.add(vote);
        }
        closeConnection();
        return al;
    }

    //修改某些教师的得票数
    public void updateVotes(String[] teacherno) throws Exception {
        initConnection();
        String sql = "UPDATE T_VOTE SET VOTE = VOTE + 1 WHERE TEACHERNO = ?";
        PreparedStatement ps = conn.prepareStatement(sql);
        for(int i = 0; i < teacherno.length; i++) {
            ps.setString(1, teacherno[i]);
            ps.executeUpdate();
        }
        closeConnection();
    }

    public void closeConnection() throws Exception {
        conn.close();
    }
}