package mqx.pojo;

public class Admin {
	private String adminID, adminName, adminPWD;

	public String getAdminID() {
		return adminID;
	}

	public void setAdminID(String adminID) {
		this.adminID = adminID;
	}

	public String getAdminName() {
		return adminName;
	}

	public void setAdminName(String adminName) {
		this.adminName = adminName;
	}

	public String getAdminPWD() {
		return adminPWD;
	}

	public void setAdminPWD(String adminPWD) {
		this.adminPWD = adminPWD;
	}

	public Admin() {
		super();

	}

	public Admin(String adminID, String adminName, String adminPWD) {
		super();
		this.adminID = adminID;
		this.adminName = adminName;
		this.adminPWD = adminPWD;
	}

	@Override
	public String toString() {
		return "Admin [adminID=" + adminID + ", adminName=" + adminName + ", adminPWD=" + adminPWD + "]";
	}

}
