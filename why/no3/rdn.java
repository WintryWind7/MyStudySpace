package why.no3;

import java.util.Random;

public class rdn {
    public static void main(String[] args){
        int[][] arr = new int[3][3];
        Random rd = new Random();
        int minN = 99;
        
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                arr[i][j] = rd.nextInt(90) + 10;
            }
        }
        
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.printf("%d ", arr[i][j]);
                if (arr[i][j] < minN){
                    minN = arr[i][j];
                }
            }
            System.out.println();
        }
        
        System.out.println("min=" + minN);
    }
}
