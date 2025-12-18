package suitang20251120;

import java.util.ArrayList;
import java.util.Collections;

public class Test {
    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        
        students.add(new Student("张三", 20));
        students.add(new Student("李四", 18));
        students.add(new Student("王五", 22));
        
        System.out.println("排序前:");
        for (Student s : students) {
            System.out.println(s);
        }
        
        Collections.sort(students);
        
        System.out.println("\n排序后(按年龄从小到大):");
        for (Student s : students) {
            System.out.println(s);
        }
    }
}




