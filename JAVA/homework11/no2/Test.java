package homework11.no2;

public class Test {
    public static void main(String[] args) {
        int totalMoney = 100;
        int packetCount = 3;
        String[] names = {"小李", "小张", "小王", "小陶", "小孙"};

        RedPacket redPacket = new RedPacket(totalMoney, packetCount);

        Thread[] threads = new Thread[names.length];
        for (int i = 0; i < names.length; i++) {
            final String name = names[i];
            threads[i] = new Thread(() -> {
                Integer money = redPacket.grab();
                if (money != null) {
                    System.out.println(name + "抢到了" + money + "元");
                } else {
                    System.out.println(name + "没有抢到红包");
                }
            });
            threads[i].start();
        }

        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}
