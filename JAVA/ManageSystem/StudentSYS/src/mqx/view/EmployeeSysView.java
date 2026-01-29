package mqx.view;
import java.util.ArrayList;
import java.util.Scanner;

import mqx.dao.EmployeeDAO;
import mqx.pojo.Employee;

public class EmployeeSysView {
	public EmployeeSysView() {
		char key, confirm;
		EmployeeDAO employeeDAO = new EmployeeDAO();
		ArrayList<Employee> employees = new ArrayList<Employee>();
		Employee employee = null;
		String empID = null;
		String empName = null;
		String department = null;
		String position = null;
		double salary = 0.0;
		Scanner input = new Scanner(System.in);
		
		while (true) {
			menu();
			key = input.next().charAt(0);
			switch (key) {
				case '1':
					System.out.println("----显示员工信息----");
					employees = employeeDAO.getAllEmployee();
					if (employees.size() == 0) {
						System.out.println("当前系统无员工，请添加后再操作");
						break;
					}
					for (Employee emp : employees) {
						System.out.println(emp);
					}
					break;
					
				case '2':
					System.out.println("----添加员工信息----");
					System.out.print("请输入工号：");
					empID = input.next();
					employee = employeeDAO.getEmployeeByID(empID);
					if (employee != null) {
						System.out.println("你输入的工号已经存在！");
						break;
					}
					System.out.print("请输入姓名：");
					empName = input.next();
					System.out.print("请输入部门：");
					department = input.next();
					System.out.print("请输入职位：");
					position = input.next();
					System.out.print("请输入薪资：");
					salary = input.nextDouble();
					
					employee = new Employee(empID, empName, department, position, salary);
					if (employeeDAO.insertEmployee(employee) > 0) {
						System.out.println("员工信息添加成功");
					} else {
						System.out.println("员工信息添加失败");
					}
					break;
					
				case '3':
					System.out.println("----查找员工信息----");
					System.out.print("请输入工号：");
					empID = input.next();
					employee = employeeDAO.getEmployeeByID(empID);
					if (employee != null) {
						System.out.println(employee);
					} else {
						System.out.println("没有找到工号为" + empID + "的信息");
					}
					break;
					
				case '4':
					System.out.println("----删除员工信息----");
					System.out.print("请输入要删除的工号：");
					empID = input.next();
					employee = employeeDAO.getEmployeeByID(empID);
					if (employee != null) {
						employeeDAO.deleteEmployee(empID);
						System.out.println("工号为" + empID + "的员工信息已删除");
					} else {
						System.out.println("没有找到工号为" + empID + "的信息");
					}
					break;
					
				case '5':
					System.out.println("----修改员工信息----");
					System.out.print("请输入要修改的工号：");
					empID = input.next();
					employee = employeeDAO.getEmployeeByID(empID);
					if (employee == null) {
						System.out.println("你输入的工号不存在！");
						break;
					}
					System.out.print("请输入姓名：");
					empName = input.next();
					System.out.print("请输入部门：");
					department = input.next();
					System.out.print("请输入职位：");
					position = input.next();
					System.out.print("请输入薪资：");
					salary = input.nextDouble();
					
					employee = new Employee(empID, empName, department, position, salary);
					if (employeeDAO.updateEmployee(employee) > 0) {
						System.out.println("员工信息修改成功");
					} else {
						System.out.println("员工信息修改失败");
					}
					break;
					
				case '6':
					System.out.println("----员工管理信息系统1.0----");
					System.out.println("作者：why");
					System.out.println("学号：2513313045");
					System.out.println("完成时间：2025年12月");
					break;

				case '0':
					System.out.print("\t确定要退出吗？（y/n）");
					confirm = input.next().charAt(0);
					if ('Y' == confirm || 'y' == confirm) {
						System.out.println("\t程序已经退出~~~~~~");
						System.exit(0);
					}
					break;
					
				default:
					System.out.println("输入错误");
					break;
			}
		}
	}
	
	public static void menu() {
		System.out.println("=========员工管理信息系统V1.0=========");
		System.out.println("\t1、显示");
		System.out.println("\t2、添加");
		System.out.println("\t3、查找");
		System.out.println("\t4、删除");
		System.out.println("\t5、修改");
		System.out.println("\t6、帮助");
		System.out.println("\t0、退出");
		System.out.print("\t请选择（0-6）：");
	}
}
