package homework11.no1;

public class Window implements Runnable {
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
