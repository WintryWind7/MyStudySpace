package homework5;
import java.util.Random;

public class no3 {
    public static void getArrayMax() {
        Random random = new Random();
        int[] array1 = new int[10];
        System.out.println("数组：");
        for (int i = 0; i < array1.length; i++) {
            array1[i] = random.nextInt(100) + 1;
            System.out.printf("%2d ", array1[i]);
        }
        
        int max1 = array1[0];
        for (int i = 1; i < array1.length; i++) {
            if (array1[i] > max1) {
                max1 = array1[i];
            }
        }
        System.out.println();
        System.out.println("最大值：" + max1);
        System.out.println();
    
    }
}