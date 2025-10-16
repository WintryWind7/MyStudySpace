public class no2 {
    public static void main(String[] args) {
        int[] numbers = new int[50];
        int count = 0;
        
        int scount;
        for (int i = 0; i < 100; i++) {
            scount = 0;
            for (int j = 1; j < i/2; j++) {
                if (i % j == 0) {
                    scount++;
                }
            }
            if (scount == 2) {
                numbers[count] = i;
                count++;
            }
        }
        for (int i = 0; i < count; i++) {
        
        if ((i+1)%5==0){
            System.out.printf("%d\n",numbers[i]);
        }else{
            System.out.printf("%d ",numbers[i]);
        }
    }
    System.out.println("\n素数个数：" + count);
    }
}
