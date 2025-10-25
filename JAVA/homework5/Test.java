package homework5;

public class Test {
    public static void main(String[] args) {
        System.out.println("=== homework5 功能测试 ===\n");
        
        System.out.println("【no1】");
        no1.gcd();
        System.out.println();
        
        System.out.println("【no2】");
        int count = 0;
        
        for (int i = 1; i <= 100; i++) {
            if (no2.isPrime(i)) {
                count++;
            }
        }
        
        System.out.println("\n100以内共有" + count + "个素数");
        System.out.println();
        
        System.out.println("【no3】");
        no3.getArrayMax();
        
    }
}
