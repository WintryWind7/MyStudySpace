package homework7.no2;

public class College extends Student {
    private int score1;
    private int score2;
    
    public College(String stuID, String stuName, int score1, int score2) {
        super(stuID, stuName);
        this.score1 = score1;
        this.score2 = score2;
    }
    
    public int getScore1() {
        return score1;
    }
    
    public void setScore1(int score1) {
        this.score1 = score1;
    }
    
    public int getScore2() {
        return score2;
    }
    
    public void setScore2(int score2) {
        this.score2 = score2;
    }
    
    @Override
    public int totalScore() {
        return score1 + score2;
    }
    
    @Override
    public String toString() {
        return "College [" + super.toString() + "], 总成绩: " + totalScore() + ",成绩明细: [score1=" + score1 + ", score2=" + score2 + "]";
    }
}
