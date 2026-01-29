package mqx.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import mqx.pojo.Employee;

public class EmployeeDAO {

	Connection conn = null;
	PreparedStatement pst = null;
	ResultSet rs = null;

	// 添加员工
	public int insertEmployee(Employee emp) {
		conn = DbHelperByMySQL.getConnection();
		String sql = "insert into employeeinfo(empID,empName,department,position,salary)values(?,?,?,?,?)";

		int i = 0;
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, emp.getEmpID());
			pst.setString(2, emp.getEmpName());
			pst.setString(3, emp.getDepartment());
			pst.setString(4, emp.getPosition());
			pst.setDouble(5, emp.getSalary());
			i = pst.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DbHelperByMySQL.close(null, pst, conn);
		}

		return i;
	}

	// 删除员工
	public int deleteEmployee(String empID) {
		conn = DbHelperByMySQL.getConnection();
		String sql = "delete from employeeinfo where empID=?";
		int i = 0;
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, empID);
			i = pst.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DbHelperByMySQL.close(null, pst, conn);
		}

		return i;
	}

	// 修改员工信息
	public int updateEmployee(Employee emp) {
		conn = DbHelperByMySQL.getConnection();
		String sql = "update employeeinfo set empName=?,department=?,position=?,salary=? where empID=?";
		int i = 0;
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, emp.getEmpName());
			pst.setString(2, emp.getDepartment());
			pst.setString(3, emp.getPosition());
			pst.setDouble(4, emp.getSalary());
			pst.setString(5, emp.getEmpID());
			i = pst.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DbHelperByMySQL.close(null, pst, conn);
		}

		return i;
	}

	// 查找所有员工
	public ArrayList<Employee> getAllEmployee() {
		conn = DbHelperByMySQL.getConnection();
		String sql = "select * from employeeinfo";
		ArrayList<Employee> employees = new ArrayList<Employee>();
		try {
			pst = conn.prepareStatement(sql);
			rs = pst.executeQuery();
			while (rs.next()) {
				String empID = rs.getString("empID");
				String empName = rs.getString("empName");
				String department = rs.getString("department");
				String position = rs.getString("position");
				double salary = rs.getDouble("salary");
				Employee emp = new Employee(empID, empName, department, position, salary);
				employees.add(emp);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DbHelperByMySQL.close(rs, pst, conn);
		}
		return employees;
	}

	// 根据工号查找员工
	public Employee getEmployeeByID(String parEmpID) {
		conn = DbHelperByMySQL.getConnection();
		String sql = "select * from employeeinfo where empID=?";
		Employee employee = null;
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, parEmpID);
			rs = pst.executeQuery();
			while (rs.next()) {
				String empID = rs.getString("empID");
				String empName = rs.getString("empName");
				String department = rs.getString("department");
				String position = rs.getString("position");
				double salary = rs.getDouble("salary");
				employee = new Employee(empID, empName, department, position, salary);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			DbHelperByMySQL.close(rs, pst, conn);
		}
		return employee;
	}
}