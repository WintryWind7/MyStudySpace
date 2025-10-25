package suitang20251023;

public class Test {
    public static void main(String[] args) {
        Student[] students = new Student[3];
        students[0] = new Student("张三", 20);
        students[1] = new Student("李四", 22);
        students[2] = new Student("王五", 19);
        
        for (Student student : students) {
            System.out.println(student.getInfo());
        }
    }
}
