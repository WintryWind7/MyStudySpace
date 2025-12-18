package homework9.no1;

public class Student {
    private String name;
    private int age;
    
    public Student() {
    }
    
    public Student(String name, int age) throws NameException, AgeException {
        setName(name);
        setAge(age);
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) throws NameException {
        if (name == null || name.length() < 2 || name.length() > 8) {
            throw new NameException("姓名长度必须在2-8之间！");
        }
        this.name = name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void setAge(int age) throws AgeException {
        if (age < 15 || age > 50) {
            throw new AgeException("年龄必须在15-50之间！");
        }
        this.age = age;
    }
    
    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
