package homework4;
import java.util.Scanner;

public class no1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("请输入第一个数：");
        int a = scanner.nextInt();
        System.out.print("请输入第二个数：");
        int b = scanner.nextInt();
        int min, gcd = 1;
        if (a>b){
            min = b;
        }else{
            min = a;
        }
        if (a%min==0 && b%min==0){
            gcd = min;
        }else{
            for (int i = 1; i <= min/2; i++) {
            if (a%i==0 && b%i==0){
                gcd = i;
                }
            }
        }
        
        System.out.println(a + "和" + b + "的最大公约数是：" + gcd);
        
        scanner.close();
    }
}
