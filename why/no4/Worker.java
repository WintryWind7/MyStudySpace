package why.no4;

public class Worker extends Employee {
    private double s1;
    
    public Worker() {
    }
    
    public Worker(String name, String title, double s1) {
        super(name, title);
        this.s1 = s1;
    }
    
    @Override
    public double totalSalary() {
        return s1;
    }
    
    public double getS1() {
        return s1;
    }
    
    public void setS1(double s1) {
        this.s1 = s1;
    }
    
    @Override
    public String toString() {
        return "工人，姓名：" + getName() + ",职位：" + getTitle() + 
               ",总薪水：" + totalSalary() + ",薪水明细：s1=" + s1;
    }
}
