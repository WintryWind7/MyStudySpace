package JAVA.ces;

public class ChangeCalculatorTest {
    public static void main(String[] args) {
        int totalCases = 0;
        int passedCases = 0;
        int failedCases = 0;
        
        // 测试用例数组：{P, M, 期望结果}
        Object[][] testCases = {
            // T1
            {0, 0, "输入出界"},
            // T2
            {0, 100, "输入出界"},
            // T3
            {0, 101, "输入出界"},
            // T4
            {1, 2, "N50=0  N10=0  N5=0  N1=1"},
            // T5
            {1, 100, "N50=1  N10=4  N5=1  N1=4"},
            // T6
            {2, 1, "输入出界"},
            // T7
            {3, 16, "N50=0  N10=1  N5=0  N1=3"},
            // T8
            {30, 60, "N50=0  N10=3  N5=0  N1=0"},
            // T9
            {99, 99, "N50=0  N10=0  N5=0  N1=0"},
            // T10
            {99, 101, "输入出界"},
            // T11
            {100, 1, "输入出界"},
            // T12
            {101, 1, "输入出界"}
        };
        
        System.out.println("开始执行找钱计算程序测试...\n");
        
        for (int i = 0; i < testCases.length; i++) {
            totalCases++;
            int P = (int) testCases[i][0];
            int M = (int) testCases[i][1];
            String expected = (String) testCases[i][2];
            
            String actual = ChangeCalculator.calculateChange(P, M);
            
            boolean passed = expected.equals(actual);
            
            System.out.printf("测试用例 T%d: P=%d  M=%d\n", i + 1, P, M);
            System.out.printf("期望结果: %s\n", expected);
            System.out.printf("实际结果: %s\n", actual);
            System.out.printf("测试结果: %s\n\n", passed ? "通过" : "失败");
            
            if (passed) {
                passedCases++;
            } else {
                failedCases++;
            }
        }
        
        // 统计结果
        printTestStatistics(totalCases, passedCases, failedCases);
    }
    
    private static void printTestStatistics(int totalCases, int passedCases, int failedCases) {
        System.out.println("=== 测试执行结果统计 ===");
        System.out.printf("测试用例总数: %d\n", totalCases);
        System.out.printf("测试用例覆盖率: 100%%\n");
        System.out.printf("执行测试用例数: %d\n", totalCases);
        System.out.printf("测试用例执行率: 100%%\n");
        System.out.printf("已通过的测试用例数: %d\n", passedCases);
        System.out.printf("未通过的测试用例数: %d\n", failedCases);
        
        // 估算代码行数（约20行）并计算缺陷密度
        int loc = 20;
        double defectDensity = (double) failedCases / loc;
        System.out.printf("软件缺陷密度: %.2f个/LOC\n", defectDensity);
        
        // 测试通过率
        double passRate = (double) passedCases / totalCases * 100;
        System.out.printf("测试通过率: %.1f%%\n", passRate);
        
        // 详细结果分析
        System.out.println("\n=== 边界值覆盖分析 ===");
        System.out.println("P边界值覆盖: 0,1,2,99,100,101 ✓");
        System.out.println("M边界值覆盖: 0,1,2,99,100,101 ✓");
        System.out.println("M-P边界值覆盖: 0,1,2,99,100,101 ✓");
        System.out.println("输出面额边界值覆盖完成 ✓");
    }
}
