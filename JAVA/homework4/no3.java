package homework4;
import java.util.Random;

public class no3 {
    public static void main(String[] args) {
        Random random = new Random();
        int[][] array = new int[3][3];
        int max = 0;
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                array[i][j] = random.nextInt(90) + 10;
                System.out.printf("%2d ", array[i][j]);
                
                // 最大值
                if (i == 0 && j == 0) {
                    max = array[i][j];
                } else if (array[i][j] > max) {
                    max = array[i][j];
                }
            }
            System.out.println();
        }
        
        System.out.println("最大值：" + max);
    }
}
