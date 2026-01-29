package why.no5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Test {
    public static void main(String[] args) {

        List<Student> list = new ArrayList<>();
        list.add(new Student("1001", 80, 70));
        list.add(new Student("1002", 90, 70));
        list.add(new Student("1003", 80, 90));
        list.add(new Student("1004", 80, 70));

        Collections.sort(list);

        for (Student student : list) {
            System.out.println(student);
        }
    }
}
