package JAVA.ces;

public class DateCalculatorTest {
    public static void main(String[] args) {
        int totalCases = 0;
        int passedCases = 0;
        int failedCases = 0;
        
        // 测试用例数组：{年份, 月份, 日期, 期望结果}
        Object[][] testCases = {
            // 正常日期测试
            {2025, 3, 15, "2025年3月17日"},
            {2025, 1, 30, "2025年2月1日"},
            {2025, 4, 29, "2025年5月1日"},
            
            // 年末边界测试
            {2025, 12, 30, "2026年1月1日"},
            {2025, 12, 31, "2026年1月2日"},
            
            // 闰年特殊测试
            {2024, 2, 27, "2024年2月29日"},
            {2024, 2, 28, "2024年3月1日"},
            {2024, 2, 29, "2024年3月2日"},
            {2023, 2, 27, "2023年3月1日"},
            
            // 异常输入测试
            {2025, 4, 31, "输入日期错误"},
            {2023, 2, 29, "输入日期错误"},
            {2025, 13, 1, "输入日期错误"},
            
            // 边界值测试
            {1000, 1, 1, "1000年1月3日"},
            {9998, 12, 30, "9999年1月1日"},
            {2025, 2, 28, "2025年3月2日"}
        };
        
        System.out.println("开始执行测试...\n");
        
        for (int i = 0; i < testCases.length; i++) {
            totalCases++;
            int year = (int) testCases[i][0];
            int month = (int) testCases[i][1];
            int day = (int) testCases[i][2];
            String expected = (String) testCases[i][3];
            
            String actual = DateCalculator.calculateNextTwoDays(year, month, day);
            
            boolean passed = expected.equals(actual);
            
            System.out.printf("测试用例 T%d: %d年%d月%d日\n", i + 1, year, month, day);
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
        System.out.println("=== 测试执行结果统计 ===");
        System.out.printf("测试用例总数: %d\n", totalCases);
        System.out.printf("测试用例覆盖率: 100%%\n");
        System.out.printf("执行测试用例数: %d\n", totalCases);
        System.out.printf("测试用例执行率: 100%%\n");
        System.out.printf("已通过的测试用例数: %d\n", passedCases);
        System.out.printf("未通过的测试用例数: %d\n", failedCases);
        
        // 估算代码行数（约50行）并计算缺陷密度
        int loc = 50; // 估算的程序代码行数
        double defectDensity = (double) failedCases / loc;
        System.out.printf("软件缺陷密度: %.2f个/LOC\n", defectDensity);
        
        // 测试通过率
        double passRate = (double) passedCases / totalCases * 100;
        System.out.printf("测试通过率: %.1f%%\n", passRate);
    }
}

