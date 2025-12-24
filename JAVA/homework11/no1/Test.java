package homework11.no1;

public class Test {
    public static void main(String[] args) {
        Window ticketSeller = new Window();

        Thread eastWindow = new Thread(ticketSeller, "窗口东");
        Thread northWindow = new Thread(ticketSeller, "窗口北");
        Thread southWindow = new Thread(ticketSeller, "窗口南");

        eastWindow.start();
        northWindow.start();
        southWindow.start();

        try {
            eastWindow.join();
            northWindow.join();
            southWindow.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
