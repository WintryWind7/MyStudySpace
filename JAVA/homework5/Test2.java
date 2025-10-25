package homework5;

public class Test2 {
    public static void main(String[] args) {
        System.out.println("【no2测试】");
        System.out.println("100以内的所有素数：");
        int count = 0;
        
        for (int i = 1; i <= 100; i++) {
            if (no2.isPrime(i)) {
                System.out.printf("%2d ", i);
                count++;
                
                if (count % 10 == 0) {
                    System.out.println();
                }
            }
        }
        
        System.out.println("\n100以内共有" + count + "个素数");
    }
}
