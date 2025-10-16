package homework4;
import java.util.Random;

public class no2 {
    public static void main(String[] args) {
        Random random = new Random();
        int[] a = new int[10];
        
        System.out.println("10个裁判的打分：");
        
        for (int i = 0; i < 10; i++) {
            a[i] = random.nextInt(10) + 1;
            System.out.print(a[i] + " ");
        }
        System.out.println();
        
        int max = a[0];
        int min = a[0];
        int sum = 0;
        
        for (int i = 0; i < 10; i++) {
            sum += a[i];
            if (a[i] > max) max = a[i];
            if (a[i] < min) min = a[i];
        }
       
        sum = sum - max - min;
        double average = sum / 8.0;
        
        System.out.println("最高分：" + max);
        System.out.println("最低分：" + min);
        System.out.printf("去掉最高分和最低分后的平均分：%.2f\n", average);
    }
}
