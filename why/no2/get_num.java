package why.no2;

public class get_num {
    public static void main(String[] args) {
        int count = 0;
        int x = 0;
        for (int i=300;i<=400;i++){
            x = 0;
            for (int j=2;j<=(i/2)+1;j++){
                if (i%j==0){
                    x = 1;
                    break;
                }
            }
            if (x != 1){
                if ((count!=0) && (count%5==0)){
                    System.out.print("\n");
                }
                System.out.printf("%d ", i);
                count ++;
            }
        }
    }
}
