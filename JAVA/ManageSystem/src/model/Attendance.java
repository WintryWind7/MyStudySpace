package model;

import java.sql.Timestamp;

public class Attendance {
	private String empID;
	private String status;
	private Timestamp lastUpdateTime;

	public String getEmpID() {
		return empID;
	}

	public void setEmpID(String empID) {
		this.empID = empID;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public Timestamp getLastUpdateTime() {
		return lastUpdateTime;
	}

	public void setLastUpdateTime(Timestamp lastUpdateTime) {
		this.lastUpdateTime = lastUpdateTime;
	}

	public Attendance() {
		super();
	}

	public Attendance(String empID, String status, Timestamp lastUpdateTime) {
		super();
		this.empID = empID;
		this.status = status;
		this.lastUpdateTime = lastUpdateTime;
	}

	@Override
	public String toString() {
		return "工号=" + empID + ", 状态=" + status + ", 更新时间=" + lastUpdateTime;
	}
}
