package why.no4;

public class Test {
    public static void main(String[] args) {
        Employee e1 = new Manager("小明", "人事部经理", 2000, 3000);
        Employee e2 = new Manager("张三", "销售部经理", 3000, 3000);
        Employee e3 = new Worker("李四", "会计", 6000);
        Employee e4 = new Worker("王五", "办公室员工", 5000);
        
        Employee[] employees = { e1, e2, e3, e4 };
        
        for (Employee e : employees) {
            System.out.println(e);
        }
    }
}
