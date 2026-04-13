package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.util.ArrayList;

import model.Attendance;
import util.DatabaseHelper;

public class AttendanceDAO {

	Connection conn = null;
	PreparedStatement pst = null;
	ResultSet rs = null;

	public int checkIn(String empID) {
		conn = DatabaseHelper.getConnection();
		String sql = "INSERT INTO attendance(empID, status) VALUES(?, '在岗') " +
					 "ON DUPLICATE KEY UPDATE status='在岗'";
		int i = 0;
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, empID);
			i = pst.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DatabaseHelper.close(null, pst, conn);
		}
		return i;
	}

	public int checkOut(String empID) {
		conn = DatabaseHelper.getConnection();
		String sql = "UPDATE attendance SET status='离岗' WHERE empID=?";
		int i = 0;
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, empID);
			i = pst.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DatabaseHelper.close(null, pst, conn);
		}
		return i;
	}

	public ArrayList<Attendance> getAllAttendance() {
		conn = DatabaseHelper.getConnection();
		String sql = "SELECT * FROM attendance ORDER BY empID";
		ArrayList<Attendance> attendances = new ArrayList<Attendance>();
		try {
			pst = conn.prepareStatement(sql);
			rs = pst.executeQuery();
			while (rs.next()) {
				String empID = rs.getString("empID");
				String status = rs.getString("status");
				Timestamp lastUpdateTime = rs.getTimestamp("lastUpdateTime");
				Attendance att = new Attendance(empID, status, lastUpdateTime);
				attendances.add(att);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DatabaseHelper.close(rs, pst, conn);
		}
		return attendances;
	}

	public Attendance getAttendanceByID(String empID) {
		conn = DatabaseHelper.getConnection();
		String sql = "SELECT * FROM attendance WHERE empID=?";
		Attendance attendance = null;
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, empID);
			rs = pst.executeQuery();
			if (rs.next()) {
				String status = rs.getString("status");
				Timestamp lastUpdateTime = rs.getTimestamp("lastUpdateTime");
				attendance = new Attendance(empID, status, lastUpdateTime);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DatabaseHelper.close(rs, pst, conn);
		}
		return attendance;
	}

	public ArrayList<Attendance> getOnDutyEmployees() {
		conn = DatabaseHelper.getConnection();
		String sql = "SELECT * FROM attendance WHERE status='在岗' ORDER BY empID";
		ArrayList<Attendance> attendances = new ArrayList<Attendance>();
		try {
			pst = conn.prepareStatement(sql);
			rs = pst.executeQuery();
			while (rs.next()) {
				String empID = rs.getString("empID");
				String status = rs.getString("status");
				Timestamp lastUpdateTime = rs.getTimestamp("lastUpdateTime");
				Attendance att = new Attendance(empID, status, lastUpdateTime);
				attendances.add(att);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DatabaseHelper.close(rs, pst, conn);
		}
		return attendances;
	}
}
