package homework7.no2;

public class Test {
    public static void main(String[] args) {
        Student stu1 = new Pupil("1001", "wetwe", 98, 100);
        System.out.println(stu1);
        Student stu2 = new College("1111", "dsfgs", 96, 95);
        System.out.println(stu2);
        System.out.println("学生总数: " + Student.number);
    }
}
