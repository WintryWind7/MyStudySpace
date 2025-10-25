public class Test {
    public static void main(String[] args) {
        System.out.println("无参构造方法");
        Student student2 = new Student();
        System.out.println(student2.toString());
        
        Student myInfo = new Student("why", 22, "2513313045");
        System.out.println(myInfo.toString());
    }
}
