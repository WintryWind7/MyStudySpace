public class Computer {
    // 加法
    public int add(int a, int b) {
        return a + b;
    }
    
    // 减法
    public int sub(int a, int b) {
        return a - b;
    }
    
    // 乘法
    public int multiply(int a, int b) {
        return a * b;
    }
    
    // 除法
    public int div(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("除数不能为零");
        }
        return a / b;
    }
}