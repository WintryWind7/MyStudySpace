package why.no5;

public class Student implements Comparable<Student> {
    private String stuID;
    private int java;
    private int python;

    public Student(String stuID, int python, int java) {
        this.stuID = stuID;
        this.python = python;
        this.java = java;
    }

    @Override
    public int compareTo(Student other) {
        if (this.python != other.python) {
            return other.python - this.python;
        }
        
        if (this.java != other.java) {
            return other.java - this.java;
        }
        
        return this.stuID.compareTo(other.stuID);
    }

    @Override
    public String toString() {
        return "Student [stuID=" + stuID  + 
               ", python=" + python  + ", java=" + java +  "]";
    }
}

