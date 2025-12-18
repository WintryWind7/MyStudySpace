package homework9.no2;

import homework9.no1.Student;
import homework9.no1.NameException;
import homework9.no1.AgeException;
import java.util.ArrayList;

public class TestStudentList {
    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        
        try {
            Student student1 = new Student("张三", 20);
            Student student2 = new Student("李四", 25);
            Student student3 = new Student("王五", 30);
            
            students.add(student1);
            students.add(student2);
            students.add(student3);
            
            System.out.println("所有学生信息：");
            System.out.println("==================");
            for (int i = 0; i < students.size(); i++) {
                System.out.println("学生" + (i + 1) + "：" + students.get(i));
            }
            
        } catch (NameException e) {
            System.out.println("姓名异常：" + e.getMessage());
        } catch (AgeException e) {
            System.out.println("年龄异常：" + e.getMessage());
        }
    }
}
