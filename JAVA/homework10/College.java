package homework10;

public class College implements Comparable<College> {
    private int stuID;
    private String stuName;
    private int java;
    private int english;
    private int os;

    public College(int stuID, String stuName, int java, int english, int os) {
        this.stuID = stuID;
        this.stuName = stuName;
        this.java = java;
        this.english = english;
        this.os = os;
    }

    public int getStuID() {
        return stuID;
    }

    public String getStuName() {
        return stuName;
    }

    public int getJava() {
        return java;
    }

    public int getEnglish() {
        return english;
    }

    public int getOs() {
        return os;
    }

    @Override
    public int compareTo(College other) {
        // 1) java成绩从小到大
        if (this.java != other.java) {
            return this.java - other.java;
        }
        
        // 2) 若java成绩相同，按照英语成绩从大到小
        if (this.english != other.english) {
            return other.english - this.english;
        }
        
        // 3) 若java、英语成绩都相同，按照操作系统成绩从小到大
        if (this.os != other.os) {
            return this.os - other.os;
        }
        
        // 4) 若三门课程成绩都相同，按照学号从小到大
        return this.stuID - other.stuID;
    }

    @Override
    public String toString() {
        return "College{stuID=" + stuID + ", stuName=" + stuName + 
               ", java=" + java + ", english=" + english + ", os=" + os + "}";
    }
}
