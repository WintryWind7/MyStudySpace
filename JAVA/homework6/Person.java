public class Person {
    private String name;
    private int age;
    
    public Person() {
    }
    
    public Person(String name, int age) {
        setName(name);
        setAge(age);
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        if (name.length() >= 2 && name.length() <= 8) {
            this.name = name;
        } else {
            System.out.println("姓名长度错误(2-8个字符)");
            System.exit(0);
        }
    }
    
    public int getAge() {
        return age;
    }
    
    public void setAge(int age) {
        if (age >= 7 && age <= 50) {
            this.age = age;
        } else {
            System.out.println("年龄输入错误(7<=x<=50)");
            System.exit(0);
        }
    }
    
    public String toString() {
        return "姓名: " + name + ", 年龄: " + age;
    }
}
