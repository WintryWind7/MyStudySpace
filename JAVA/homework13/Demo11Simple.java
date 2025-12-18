package homework13;

import java.util.Scanner;

public class Demo11Simple {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入学号:");
        String stuID = scanner.nextLine();
        System.out.print("请输入姓名:");
        String stuName = scanner.nextLine();
        System.out.println("添加成功");
        scanner.close();
    }
}
