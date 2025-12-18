package homework9.no1;

import java.util.Scanner;

public class TestStudent {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Student student = new Student();
        
        while (true) {
            try {
                System.out.print("请输入姓名（长度2-8）：");
                String name = scanner.nextLine();
                student.setName(name);
                break;
            } catch (NameException e) {
                System.out.println("错误：" + e.getMessage());
            }
        }
        
        while (true) {
            try {
                System.out.print("请输入年龄（15-50）：");
                String ageStr = scanner.nextLine();
                int age = Integer.parseInt(ageStr);
                student.setAge(age);
                break;
            } catch (AgeException e) {
                System.out.println("错误：" + e.getMessage());
            } catch (NumberFormatException e) {
                System.out.println("错误：请输入有效的数字！");
            }
        }
        
        System.out.println("\n学生信息录入成功：");
        System.out.println(student);
        
        scanner.close();
    }
}
