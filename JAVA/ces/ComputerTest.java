import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ComputerTest {
    // 创建测试对象
    private Computer calculator = new Computer();
    
    // 测试加法
    @Test
    public void testAdd() {
        assertEquals(5, calculator.add(2, 3));
        assertEquals(-1, calculator.add(-2, 1));
        assertEquals(0, calculator.add(0, 0));
        assertEquals(100, calculator.add(50, 50));
    }
    
    // 测试减法
    @Test
    public void testSub() {
        assertEquals(1, calculator.sub(3, 2));
        assertEquals(-1, calculator.sub(2, 3));
        assertEquals(0, calculator.sub(5, 5));
        assertEquals(-5, calculator.sub(0, 5));
    }
    
    // 测试乘法
    @Test
    public void testMultiply() {
        assertEquals(6, calculator.multiply(2, 3));
        assertEquals(0, calculator.multiply(0, 5));
        assertEquals(-6, calculator.multiply(2, -3));
        assertEquals(25, calculator.multiply(5, 5));
    }
    
    // 测试除法
    @Test
    public void testDiv() {
        assertEquals(2, calculator.div(6, 3));
        assertEquals(0, calculator.div(0, 5));
        assertEquals(-2, calculator.div(6, -3));
        assertEquals(5, calculator.div(10, 2));
    }
    
    // 测试除零异常
    @Test
    public void testDivByZero() {
        assertThrows(ArithmeticException.class, () -> {
            calculator.div(5, 0);
        });
    }
}