package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import model.Admin;
import util.DatabaseHelper;

public class AdminDAO {
	Connection conn = null;
	PreparedStatement pst = null;
	ResultSet rs = null;

	public int insertAdmin(Admin admin) {
		conn = DatabaseHelper.getConnection();
		String sql = "insert into adminInfo(adminid,adminName,adminPWD)values(?,?,?)";
		int i = 0;
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, admin.getAdminID());
			pst.setString(2, admin.getAdminName());
			pst.setString(3, admin.getAdminPWD());
			i = pst.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DatabaseHelper.close(null, pst, conn);
		}
		return i;
	}

	public Admin getAdminByID(String parAdminID) {
		conn = DatabaseHelper.getConnection();
		String sql = "select * from adminInfo where adminID=?";
		Admin admin = null;
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, parAdminID);
			rs = pst.executeQuery();
			while (rs.next()) {
				String adminID = rs.getString("adminID");
				String adminName = rs.getString("adminName");
				String adminPWD = rs.getString("adminPWD");
				admin = new Admin(adminID, adminName, adminPWD);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DatabaseHelper.close(rs, pst, conn);
		}
		return admin;
	}
}
