package why.no4;

public class Manager extends Employee {
    private double s1;
    private double s2;
    
    public Manager() {
    }
    
    public Manager(String name, String title, double s1, double s2) {
        super(name, title);
        this.s1 = s1;
        this.s2 = s2;
    }
    
    @Override
    public double totalSalary() {
        return s1 + s2;
    }
    
    public double getS1() {
        return s1;
    }
    
    public void setS1(double s1) {
        this.s1 = s1;
    }
    
    public double getS2() {
        return s2;
    }
    
    public void setS2(double s2) {
        this.s2 = s2;
    }
    
    @Override
    public String toString() {
        return "经理，姓名：" + getName() + ",职位：" + getTitle() + 
               ",总薪水：" + totalSalary() + ",薪水明细：s1=" + s1 + ", s2=" + s2;
    }
}
