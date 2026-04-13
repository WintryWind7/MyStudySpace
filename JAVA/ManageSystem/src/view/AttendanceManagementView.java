package view;

import java.util.ArrayList;
import java.util.Scanner;

import dao.AttendanceDAO;
import dao.EmployeeDAO;
import model.Attendance;
import model.Employee;

public class AttendanceManagementView {
	public AttendanceManagementView() {
		char key;
		AttendanceDAO attendanceDAO = new AttendanceDAO();
		EmployeeDAO employeeDAO = new EmployeeDAO();
		ArrayList<Attendance> attendances = new ArrayList<Attendance>();
		Attendance attendance = null;
		Employee employee = null;
		String empID = null;
		Scanner input = new Scanner(System.in);

		while (true) {
			attendanceMenu();
			key = input.next().charAt(0);
			switch (key) {
			case '1':
				System.out.println();
				System.out.println("----显示所有考勤状态----");
				attendances = attendanceDAO.getAllAttendance();
				if (attendances.size() == 0) {
					System.out.println("当前系统无考勤记录");
					break;
				}
				for (Attendance att : attendances) {
					System.out.println(att);
				}
				break;

			case '2':
				System.out.println();
				System.out.println("----员工签到----");
				System.out.print("请输入工号：");
				empID = input.next();

				employee = employeeDAO.getEmployeeByID(empID);
				if (employee == null) {
					System.out.println("工号 " + empID + " 不存在，请先添加员工信息");
					break;
				}

				attendance = attendanceDAO.getAttendanceByID(empID);
				if (attendance != null && "在岗".equals(attendance.getStatus())) {
					System.out.println("员工 " + employee.getEmpName() + " 已经在岗，无需重复签到");
					break;
				}

				if (attendanceDAO.checkIn(empID) > 0) {
					System.out.println("员工 " + employee.getEmpName() + " 签到成功，当前状态：在岗");
				} else {
					System.out.println("签到失败");
				}
				break;

			case '3':
				System.out.println();
				System.out.println("----员工签退----");
				System.out.print("请输入工号：");
				empID = input.next();

				employee = employeeDAO.getEmployeeByID(empID);
				if (employee == null) {
					System.out.println("工号 " + empID + " 不存在");
					break;
				}

				attendance = attendanceDAO.getAttendanceByID(empID);
				if (attendance == null || "离岗".equals(attendance.getStatus())) {
					System.out.println("员工 " + employee.getEmpName() + " 已经离岗，无需重复签退");
					break;
				}

				if (attendanceDAO.checkOut(empID) > 0) {
					System.out.println("员工 " + employee.getEmpName() + " 签退成功，当前状态：离岗");
				} else {
					System.out.println("签退失败");
				}
				break;

			case '4':
				System.out.println();
				System.out.println("----查询员工状态----");
				System.out.print("请输入工号：");
				empID = input.next();

				employee = employeeDAO.getEmployeeByID(empID);
				if (employee == null) {
					System.out.println("工号 " + empID + " 不存在");
					break;
				}

				attendance = attendanceDAO.getAttendanceByID(empID);
				if (attendance != null) {
					System.out.println("员工姓名：" + employee.getEmpName());
					System.out.println(attendance);
				} else {
					System.out.println("该员工暂无考勤记录");
				}
				break;

			case '5':
				System.out.println();
				System.out.println("----显示在岗员工----");
				attendances = attendanceDAO.getOnDutyEmployees();
				if (attendances.size() == 0) {
					System.out.println("当前无在岗员工");
					break;
				}
				System.out.println("当前在岗员工数：" + attendances.size());
				for (Attendance att : attendances) {
					employee = employeeDAO.getEmployeeByID(att.getEmpID());
					if (employee != null) {
						System.out.println("工号=" + att.getEmpID() + ", 姓名=" + employee.getEmpName() + ", 部门="
								+ employee.getDepartment() + ", 状态=" + att.getStatus());
					}
				}
				break;

			case '0':
				System.out.println("返回主菜单");
				return;

			default:
				System.out.println("输入错误");
				break;
			}
		}
	}

	public static void attendanceMenu() {
		System.out.println();
		System.out.println("=========考勤管理系统=========");
		System.out.println("\t1、显示所有考勤状态");
		System.out.println("\t2、员工签到");
		System.out.println("\t3、员工签退");
		System.out.println("\t4、查询员工状态");
		System.out.println("\t5、显示在岗员工");
		System.out.println("\t0、返回主菜单");
		System.out.print("\t请选择（0-5）：");
	}
}
