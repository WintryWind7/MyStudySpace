package JAVA.ces;
public class ChangeCalculator {
    
    public static String calculateChange(int P, int M) {
        // 输入验证
        if (P < 1 || P > 100 || M < 1 || M > 100 || P > M) {
            return "输入出界";
        }
        
        int change = M - P;
        
        // 计算各面额张数
        int n50 = change / 50;
        change = change % 50;
        
        int n10 = change / 10;
        change = change % 10;
        
        int n5 = change / 5;
        change = change % 5;
        
        int n1 = change;
        
        return String.format("N50=%d  N10=%d  N5=%d  N1=%d", n50, n10, n5, n1);
    }
}
