package why.no1;

public interface Window extends Runnable{} 

public class Ticket implements Window {
    private static final int TOTAL_TICKETS = 10;

    private int nextTicket = 1;
    private final Object lock = new Object();

    @Override
    public void run() {
        while (true) {
            int ticketNumber;
            synchronized (lock) {
                if (nextTicket > TOTAL_TICKETS) {
                    break;
                }
                ticketNumber = nextTicket++;
            }
            System.out.println(Thread.currentThread().getName() + " 正在售出第" + ticketNumber + "张票");
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }

}

public class Test{
    public static void main(String[] args) {
        Ticket ticketSeller = new Ticket();

        Thread eastWindow = new Thread(ticketSeller, "雨花");
        Thread northWindow = new Thread(ticketSeller, "浦口");
        Thread southWindow = new Thread(ticketSeller, "江宁");

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