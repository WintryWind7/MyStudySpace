package suitang20251023;

public class Test {
    public static void main(String[] args) {
        Student[] students = new Student[3];
        
        students[0] = new Student();
        students[0].setName("张三");
        students[0].setAge(7);
        System.out.println(students[0].getInfo());
        
        students[1] = new Student();
        students[1].setName("李四");
        students[1].setAge(22);
        System.out.println(students[1].getInfo());
        
        students[2] = new Student();
        students[2].setName("王五");
        students[2].setAge(100);
        System.out.println(students[2].getInfo());
    }
}
