package suitang20251023;

public class Student {
    private String name;
    private int age;
    
    public Student() {
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public void setAge(int age) {
        if (age >= 7 && age <= 50) {
            this.age = age;
        }else{
            System.out.println("年龄输入错误(7<=x<=50)");
            System.exit(0);
        }
    }
    
    public String getInfo() {
        return "姓名: " + name + ", 年龄: " + age;
    }
}
