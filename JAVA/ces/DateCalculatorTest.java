package JAVA.ces;

public class DateCalculatorTest {
    public static void main(String[] args) {
        String[][] testCases = {
            {"T1",  "R1",  "2023-01-15", "2023-01-16"},
            {"T2",  "R2",  "2023-01-30", "2023-01-31"},
            {"T3",  "R3",  "2023-01-31", "2023-02-01"},
            {"T4",  "R4",  "2023-04-15", "2023-04-16"},
            {"T5",  "R5",  "2023-04-30", "2023-05-01"},
            {"T6",  "R6",  "2023-02-15", "2023-02-16"},
            {"T7",  "R7",  "2020-01-15", "2020-01-16"},
            {"T8",  "R8",  "2020-01-30", "2020-01-31"},
            {"T9",  "R9",  "2020-01-31", "2020-02-01"},
            {"T10", "R10", "2020-04-15", "2020-04-16"},
            {"T11", "R11", "2020-04-30", "2020-05-01"},
            {"T12", "R12", "2020-02-15", "2020-02-16"},
            {"T13", "R13", "2023-02-28", "2023-03-01"},
            {"T14", "R14", "2020-02-29", "2020-03-01"},
            {"T15", "R15", "2023-12-15", "2023-12-16"},
            {"T16", "R16", "2023-12-31", "2024-01-01"},
            {"T17", "R17", "2020-12-31", "2021-01-01"}
        };
        
        // 输出表头
        System.out.println("测试用例编号\t决策表规则编号\t测试用例\t预期执行结果\t实际执行结果\t测试状态");
        System.out.println("--------------------------------------------------------------------------------");
        
        // 执行并输出
        for (String[] testCase : testCases) {
            String testId = testCase[0];
            String rule = testCase[1];
            String input = testCase[2];
            String expected = testCase[3];
            
            String[] dateParts = input.split("-");
            int year = Integer.parseInt(dateParts[0]);
            int month = Integer.parseInt(dateParts[1]);
            int day = Integer.parseInt(dateParts[2]);
            
            String actual = DateCalculator.getNextDay(year, month, day);
            String status = actual.equals(expected) ? "通过" : "失败";
            
            System.out.printf("%s\t%s\t%s\t%s\t%s\t%s%n", 
                testId, rule, input, expected, actual, status);
        }
    }
}