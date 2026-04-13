package view;

import java.util.Scanner;

import dao.AdminDAO;
import model.Admin;

public class LoginView {
	AdminDAO adminDAO = new AdminDAO();
	Admin admin = null;
	private char key = ' ';
	Scanner input = new Scanner(System.in);
	String adminID = null;
	String adminName = null;
	String adminPWD = null;

	public LoginView() {
		while (true) {
			System.out.println();
			System.out.println("====ManageSystem 管理系统====");
			System.out.println(" 1 登录");
			System.out.println(" 2 注册");
			System.out.println(" 0 退出");
			System.out.print("请输入（0-2）:");
			Scanner input = new Scanner(System.in);
			key = input.next().charAt(0);
			switch (key) {
			case '1':
				System.out.println();
				System.out.println("=======管理员登录=======");
				boolean loginSuccess = false;
				while (true) {
					System.out.print("请输入账号（输入0返回）：");
					adminID = input.next();
					if ("0".equals(adminID)) {
						System.out.println("返回主菜单");
						break;
					}
					admin = adminDAO.getAdminByID(adminID);
					if (admin != null) {
						// 账号存在，进入密码验证
						while (true) {
							System.out.print("请输入密码（输入0返回）：");
							adminPWD = input.next();
							if ("0".equals(adminPWD)) {
								System.out.println("返回账号输入");
								break;
							}
							if (admin.getAdminPWD().trim().equals(adminPWD)) {
								System.out.println("登录成功！欢迎 " + admin.getAdminName());
								loginSuccess = true;
								break;
							}
							System.out.println("密码不正确，请重新输入");
						}
						if (loginSuccess) {
							break;
						}
					} else {
						System.out.println("账号不存在，请重新输入");
					}
				}
				if (loginSuccess) {
					new EmployeeManagementView();
				}
				break;
			case '2':
				System.out.println();
				System.out.println("=====管理员注册======");
				boolean registerSuccess = false;
				while (true) {
					System.out.print("请输入账号（输入0返回）：");
					adminID = input.next();
					if ("0".equals(adminID)) {
						System.out.println("返回主菜单");
						break;
					}
					if (adminDAO.getAdminByID(adminID) == null) {
						// 账号可用，继续注册流程
						System.out.print("请输入姓名：");
						adminName = input.next();

						while (true) {
							System.out.print("请输入密码（输入0返回）：");
							adminPWD = input.next();
							if ("0".equals(adminPWD)) {
								System.out.println("返回账号输入");
								break;
							}
							System.out.print("请输入确认密码：");
							String confirmAdminPWD = input.next();
							if (adminPWD.equals(confirmAdminPWD)) {
								admin = new Admin(adminID, adminName, adminPWD);
								if (adminDAO.insertAdmin(admin) > 0) {
									System.out.println("管理员信息注册成功！");
									registerSuccess = true;
								} else {
									System.out.println("管理员信息注册失败");
								}
								break;
							}
							System.out.println("两次密码不一致，请重新输入");
						}
						break;
					} else {
						System.out.println("账号已经存在，请重新输入");
					}
				}
				break;
			case '0':
				System.out.println("你已经退出");
				System.exit(0);
				break;
			default:
				System.out.println("输入错误");
				break;
			}
		}
	}
}
