package homework7.no2;

public class Pupil extends Student {
    private int chinese;
    private int math;
    
    public Pupil(String stuID, String stuName, int chinese, int math) {
        super(stuID, stuName);
        this.chinese = chinese;
        this.math = math;
    }
    
    public int getChinese() {
        return chinese;
    }
    
    public void setChinese(int chinese) {
        this.chinese = chinese;
    }
    
    public int getMath() {
        return math;
    }
    
    public void setMath(int math) {
        this.math = math;
    }
    
    @Override
    public int totalScore() {
        return chinese + math;
    }
    
    @Override
    public String toString() {
        return "Pupil [" + super.toString() + "], 总成绩: " + totalScore() + "成绩明细: [chinese=" + chinese + ", math=" + math + "]";
    }
}
