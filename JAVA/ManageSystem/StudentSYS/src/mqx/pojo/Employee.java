package mqx.pojo;

public class Employee {
	private String empID, empName, department, position;
	private double salary;

	public String getEmpID() {
		return empID;
	}

	public void setEmpID(String empID) {
		this.empID = empID;
	}

	public String getEmpName() {
		return empName;
	}

	public void setEmpName(String empName) {
		this.empName = empName;
	}

	public String getDepartment() {
		return department;
	}

	public void setDepartment(String department) {
		this.department = department;
	}

	public String getPosition() {
		return position;
	}

	public void setPosition(String position) {
		this.position = position;
	}

	public double getSalary() {
		return salary;
	}

	public void setSalary(double salary) {
		this.salary = salary;
	}

	public Employee() {
		super();
	}

	public Employee(String empID, String empName, String department, String position, double salary) {
		super();
		this.empID = empID;
		this.empName = empName;
		this.department = department;
		this.position = position;
		this.salary = salary;
	}

	@Override
	public String toString() {
		return "工号=" + empID + ", 姓名=" + empName + ", 部门=" + department + 
			   ", 职位=" + position + ", 薪资=" + salary;
	}
}