package JAVA.ces;

import java.util.Scanner;

public class DateCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("输入日期(年 月 日): ");
        int year = scanner.nextInt();
        int month = scanner.nextInt();
        int day = scanner.nextInt();
        
        // 基本输入验证
        if (year < 1000 || year > 9998) {
            System.out.println("输入日期错误");
            return;
        }
        
        if (month < 1 || month > 12) {
            System.out.println("输入日期错误");
            return;
        }
        
        String result = calculateNextTwoDays(year, month, day);
        System.out.println(result);
    }
    
    public static String calculateNextTwoDays(int year, int month, int day) {
        // 检查日期有效性
        if (!isValidDate(year, month, day)) {
            return "输入日期错误";
        }
        
        // 计算后天
        int newDay = day + 2;
        int newMonth = month;
        int newYear = year;
        
        int daysInMonth = getDaysInMonth(year, month);
        
        if (newDay > daysInMonth) {
            newDay = newDay - daysInMonth;
            newMonth++;
            
            if (newMonth > 12) {
                newMonth = 1;
                newYear++;
                
                if (newYear > 9998) {
                    return "输入日期错误"; // 年份超限
                }
            }
        }
        
        return newYear + "年" + newMonth + "月" + newDay + "日";
    }
    
    private static boolean isValidDate(int year, int month, int day) {
        if (year < 1000 || year > 9998) return false;
        if (month < 1 || month > 12) return false;
        if (day < 1) return false;
        
        int daysInMonth = getDaysInMonth(year, month);
        return day <= daysInMonth;
    }
    
    private static int getDaysInMonth(int year, int month) {
        switch (month) {
            case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                return 31;
            case 4: case 6: case 9: case 11:
                return 30;
            case 2:
                return isLeapYear(year) ? 29 : 28;
            default:
                return 0;
        }
    }
    
    private static boolean isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }
}
