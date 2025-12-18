package JAVA.ces;
public class ChangeCalculatorTest {
    public static void main(String[] args) {
        // 定义16个测试用例
        Object[][] testCases = {
            // 测试用例编号, 价格P, 付款M, 覆盖的边界值, 预期结果字符串
            {1, 0, 1, "P1,M2,MP2", "N50=0  N10=0  N5=0  N1=1"},
            {2, 1, 100, "P2,M4,MP3", "N50=1  N10=4  N5=1  N1=4"},
            {3, 99, 100, "P3,M3,MP2", "N50=0  N10=0  N5=0  N1=1"},
            {4, 0, 100, "P1,M4,MP4", "N50=2  N10=0  N5=0  N1=0"},
            {5, 0, 0, "P1,M1,MP1", "N50=0  N10=0  N5=0  N1=0"},
            {6, 100, 100, "P4,M4,MP1", "N50=0  N10=0  N5=0  N1=0"},
            {7, 101, 100, "P5,M4,MP5", "N50=0  N10=0  N5=0  N1=0"},
            {8, -1, 100, "P6,M4,MP6", "N50=0  N10=0  N5=0  N1=0"},
            {9, 0, -1, "P1,M6,MP6", "N50=0  N10=0  N5=0  N1=0"},
            {10, 0, 101, "P1,M5,MP4", "N50=0  N10=0  N5=0  N1=0"},
            {11, 1, 0, "P2,M1,MP5", "N50=0  N10=0  N5=0  N1=0"},
            {12, 50, 100, "边界值", "N50=1  N10=0  N5=0  N1=0"},
            {13, 25, 50, "边界值", "N50=0  N10=2  N5=1  N1=0"},
            {14, 36, 50, "边界值", "N50=0  N10=1  N5=0  N1=4"},
            {15, 0, 14, "边界值", "N50=0  N10=1  N5=0  N1=4"},
            {16, 96, 100, "边界值", "N50=0  N10=0  N5=0  N1=4"}
        };
        
        // 输出测试结果
        printTestResults(testCases);
    }
    
    private static void printTestResults(Object[][] testCases) {
        // 输出格式化的测试结果
        System.out.println("测试用例表 2");
        System.out.println("测试用");
        System.out.println("例编号\t测试用例\t覆盖的边界值编号\t预期执行结果\t实际执行结果");
        
        for (Object[] testCase : testCases) {
            int testNum = (int) testCase[0];
            int price = (int) testCase[1];
            int payment = (int) testCase[2];
            String boundaries = (String) testCase[3];
            String expected = (String) testCase[4];
            
            // 计算实际结果
            int[] change = ChangeCalculator.calculateChange(price, payment);
            String actual = ChangeCalculator.formatResult(change);
            
            // 输出结果
            System.out.printf("T%d\tP=%d  M=%d\t%s\t%s\t%s%n", 
                testNum, price, payment, boundaries, expected, actual);
        }
        
    }
}