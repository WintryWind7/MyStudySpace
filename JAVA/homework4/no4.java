package homework4;
import java.util.Random;

public class no4 {
    public static void main(String[] args) {
        Random random = new Random();
        
        int[][] array = new int[5][];
        array[0] = new int[1];
        array[1] = new int[2];
        array[2] = new int[3];
        array[3] = new int[4];
        array[4] = new int[5];
    
        
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < array[i].length; j++) {
                array[i][j] = random.nextInt(90) + 10;
                System.out.printf("%2d ", array[i][j]);
            }
            System.out.println();
        }
    }
}
