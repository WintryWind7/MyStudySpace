package homework7.no1;

public class Test {
    public static void main(String[] args) {
        Student student1 = new Student("jack", 20);
        Student student2 = new Student("jack", 20);
        Student student3 = new Student("张三", 25);
        
        System.out.println(student1.toString());
        System.out.println(student2.toString());
        System.out.println(student1.equals(student2));
        System.out.println(student1.equals(student3));
    }
}
