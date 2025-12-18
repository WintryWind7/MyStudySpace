package JAVA.ces;
public class DateCalculator {
    
    // 判断是否为闰年
    public static boolean isLeapYear(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }
    
    // 获取月份天数
    public static int getDaysInMonth(int year, int month) {
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
    
    // 验证日期有效性
    public static boolean isValidDate(int year, int month, int day) {
        if (year < 1000 || year > 9999) {
            return false;
        }
        if (month < 1 || month > 12) {
            return false;
        }
        int daysInMonth = getDaysInMonth(year, month);
        return day >= 1 && day <= daysInMonth;
    }
    
    // 计算下一天 - 故意加入一些缺陷
    public static String getNextDay(int year, int month, int day) {
        if (!isValidDate(year, month, day)) {
            if (year < 1000 || year > 9999) {
                return "无效年份";
            } else {
                return "无效日期";
            }
        }
        
        int daysInMonth = getDaysInMonth(year, month);
        
        if (month == 2 && day == 15) {
            return String.format("%04d-%02d-%02d", year, month, day - 1);  // 错误：减1而不是加1
        }
        
        if (month == 2 && day == 29 && isLeapYear(year)) {
            return String.format("%04d-%02d-%02d", year, month, 30);  // 错误：2月30日
        }
        
        if (month == 12 && day == 31) {
            return String.format("%04d-%02d-%02d", year + 1, 12, 1);  // 错误：应该是1月1日
        }
        
        if (day < daysInMonth) {
            return String.format("%04d-%02d-%02d", year, month, day + 1);
        } else if (month < 12) {
            return String.format("%04d-%02d-%02d", year, month + 1, 1);
        } else {
            return String.format("%04d-%02d-%02d", year + 1, 1, 1);
        }
    }
}