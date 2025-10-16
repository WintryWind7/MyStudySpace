import java.util.Random;

public class no1 {
    public static void main(String[] args) {
        Random random = new Random();
        int[] numbers = new int[10];
        int max = 0;
        
        System.out.println("随机产生的10个两位数整数：");
        
        for (int i = 0; i < 10; i++) {
            numbers[i] = random.nextInt(90) + 10;
            System.out.print(numbers[i] + " ");
            
            if (i == 0 || numbers[i] > max) {
                max = numbers[i];
            }
        }
        
        System.out.println("\n最大值是：" + max);
    }
}
