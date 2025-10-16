package homework4;
import java.util.Scanner;

public class no1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("请输入第一个数：");
        int a = scanner.nextInt();
        System.out.print("请输入第二个数：");
        int b = scanner.nextInt();
        // 辗转相除法
        int gcd = 0;
        while (b != 0) {
            int temp = b;
            b = a % b;
            gcd = temp;
        }
        System.out.printf("最大公约数是：%d",gcd);
        
        scanner.close();
    }
}
