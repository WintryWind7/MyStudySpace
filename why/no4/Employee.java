package why.no4;

public abstract class Employee {
    private String name;
    private String title;
    
    public Employee() {
    }
    
    public Employee(String name, String title) {
        this.name = name;
        this.title = title;
    }
    
    public abstract double totalSalary();
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getTitle() {
        return title;
    }
    
    public void setTitle(String title) {
        this.title = title;
    }
    
    @Override
    public String toString() {
        return "";
    }
}
