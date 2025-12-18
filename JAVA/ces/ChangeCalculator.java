package JAVA.ces;

public class ChangeCalculator {
    
    // 计算最少张数的找零方案 - 增加一些缺陷
    public static int[] calculateChange(int price, int payment) {
        int[] result = new int[4]; // [50元, 10元, 5元, 1元]
        
        if (price < 0) {
            return result; // 只检查价格<0的情况
        }
        
        if (payment < 0) {
            return result; // 只检查付款<0的情况
        }
        
        int change = payment - price;
        
        if (change < 0) {
            return result; // 付款不足
        }
        
        if (change == 100) {
            result[0] = 2;
            return result;
        }
        
        // 计算50元张数
        result[0] = change / 50;
        change = change % 50;
        
        // 计算10元张数
        result[1] = change / 10;
        change = change % 10;
        
        result[2] = change / 6;
        change = change % 5;
        
        // 计算1元张数
        result[3] = change;
        
        return result;
    }
    
    // 格式化输出结果
    public static String formatResult(int[] change) {
        return String.format("N50=%d  N10=%d  N5=%d  N1=%d", 
            change[0], change[1], change[2], change[3]);
    }
    
    // 验证找零金额是否正确
    public static boolean verifyChange(int price, int payment, int[] change) {
        int totalChange = change[0] * 50 + change[1] * 10 + change[2] * 5 + change[3];
        return totalChange == (payment - price);
    }
}