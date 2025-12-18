package why.no3;

import java.util.*;

class Student implements Comparable<Student> {
    private String stuID;
    private String stuName;
    private int stuScore;
    
    public Student() {}
    
    public Student(String stuID, String stuName, int stuScore) {
        this.stuID = stuID;
        this.stuName = stuName;
        setStuScore(stuScore);
    }
    
    public String getStuID() { return stuID; }
    public void setStuID(String stuID) { this.stuID = stuID; }
    
    public String getStuName() { return stuName; }
    public void setStuName(String stuName) { this.stuName = stuName; }
    
    public int getStuScore() { return stuScore; }
    
    public void setStuScore(int stuScore) {
        if (stuScore < 0 || stuScore > 100) {
            System.out.println("成绩错误，程序结束");
            System.exit(0);
        }
        this.stuScore = stuScore;
    }
    
    @Override
    public String toString() {
        return stuID + " " + stuName + " " + stuScore;
    }
    
    @Override
    public int compareTo(Student o) {
        if (this.stuScore != o.stuScore) {
            return o.stuScore - this.stuScore;
        }
        if (this.stuName.length() != o.stuName.length()) {
            return this.stuName.length() - o.stuName.length();
        }
        return this.stuID.compareTo(o.stuID);
    }
}

public class Test {
    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        students.add(new Student("1001", "zhanghua", 95));
        students.add(new Student("1002", "zhanghong", 100));
        students.add(new Student("1003", "wangwei", 95));
        students.add(new Student("1004", "lifang", 90));
        students.add(new Student("1005", "libo", 90));
        students.add(new Student("1006", "lifang", 90));
        students.add(new Student("1008", "w", 45));
        
        Collections.sort(students);
        
        for (Student s : students) {
            System.out.println(s);
        }
    }
}