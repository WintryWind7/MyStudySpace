package homework5;
import java.util.Scanner;

public class no1 {
    public static void gcd() {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("请输入第一个数：");
        int a = scanner.nextInt();
        System.out.print("请输入第二个数：");
        int b = scanner.nextInt();
        
        int num1 = a, num2 = b;
        
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        
        System.out.println(num1 + "和" + num2 + "的最大公约数是：" + a);
        scanner.close();
    }
}