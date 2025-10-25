public class Student extends Person {
    private String stuID;
    
    public Student() {
        super();
    }
    
    public Student(String name, int age, String stuID) {
        super(name, age);
        setStuID(stuID);
    }
    
    public String getStuID() {
        return stuID;
    }
    
    public void setStuID(String stuID) {
        if (stuID.length() == 10) {
            this.stuID = stuID;
        } else {
            System.out.println("学号长度错误(必须为10位)");
            System.exit(0);
        }
    }
    
    public String toString() {
        return super.toString() + ", 学号: " + stuID;
    }
}
