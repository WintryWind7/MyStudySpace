public class TicketSystem {
    public static void main(String[] args) {
        TicketCounter counter = new TicketCounter(10);
        
        new Thread(new TicketSeller(counter, "北京")).start();
        new Thread(new TicketSeller(counter, "上海")).start();
        new Thread(new TicketSeller(counter, "南京")).start();
    }
}

class TicketCounter {
    private int tickets;
    
    public TicketCounter(int tickets) {
        this.tickets = tickets;
    }
    
    public synchronized boolean sellTicket(String windowName) {
        if (tickets <= 0) {
            return false;
        }
        
        System.out.println(windowName + "窗口售出第" + tickets + "张车票");
        tickets--;
        return true;
    }
}

class TicketSeller implements Runnable {
    private final TicketCounter counter;
    private final String windowName;
    
    public TicketSeller(TicketCounter counter, String windowName) {
        this.counter = counter;
        this.windowName = windowName;
    }
    
    public void run() {
        while (true) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                return;
            }
            
            if (!counter.sellTicket(windowName)) {
                break;
            }
        }
    }
}

