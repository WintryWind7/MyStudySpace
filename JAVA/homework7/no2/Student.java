package homework7.no2;

public abstract class Student {
    private String stuID;
    private String stuName;
    public static int number = 0;
    
    public Student(String stuID, String stuName) {
        this.stuID = stuID;
        this.stuName = stuName;
        number++;
    }
    
    public String getStuID() {
        return stuID;
    }
    
    public void setStuID(String stuID) {
        this.stuID = stuID;
    }
    
    public String getStuName() {
        return stuName;
    }
    
    public void setStuName(String stuName) {
        this.stuName = stuName;
    }
    
    public abstract int totalScore();
    
    @Override
    public String toString() {
        return "stuID=" + stuID + ", stuName=" + stuName;
    }
}
