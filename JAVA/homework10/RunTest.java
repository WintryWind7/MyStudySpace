import homework10.College;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class RunTest {
    public static void main(String[] args) {
        College c1 = new College(10, "wangli", 89, 78, 88);
        College c2 = new College(28, "Katefd", 89, 68, 88);
        College c3 = new College(35, "Caoyue", 69, 78, 86);
        College c4 = new College(36, "zhansa", 69, 78, 83);
        College c5 = new College(47, "wanhua", 98, 88, 88);
        College c6 = new College(52, "wanhai", 69, 88, 89);
        College c7 = new College(63, "liwuab", 89, 78, 88);

        List<College> students = new ArrayList<>();
        students.add(c1);
        students.add(c2);
        students.add(c3);
        students.add(c4);
        students.add(c5);
        students.add(c6);
        students.add(c7);

        Collections.sort(students);

        for (College student : students) {
            System.out.println(student);
        }
    }
}
