package homework8;

import java.util.Scanner;

public class Divider {
    private static String formatNumber(double value) {
        if (value == Math.rint(value)) {
            return String.format("%.0f", value);
        }
        return Double.toString(value);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double firstNumber;
        double secondNumber;

        while (true) {
            System.out.print("请输入第一个数: ");
            String input = scanner.nextLine().trim();
            try {
                firstNumber = Double.parseDouble(input);
                break;
            } catch (NumberFormatException e) {
                System.out.println("输入的不是数字，请重新输入");
            }
        }

        while (true) {
            System.out.print("请输入第二个数: ");
            String input = scanner.nextLine().trim();
            try {
                secondNumber = Double.parseDouble(input);
                if (secondNumber == 0) {
                    System.out.println("除数不能为0，请重新输入");
                    continue;
                }
                break;
            } catch (NumberFormatException e) {
                System.out.println("输入的不是数字，请重新输入");
            }
        }

        double result = firstNumber / secondNumber;
        System.out.println(formatNumber(firstNumber) + "/" + formatNumber(secondNumber) + "=" + formatNumber(result));
    }
}
