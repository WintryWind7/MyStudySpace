package homework11.no2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class RedPacket {
    private final List<Integer> packets;

    public RedPacket(int totalMoney, int count) {
        packets = new ArrayList<>();
        int remaining = totalMoney;
        int remainingCount = count;
        while (remainingCount > 1) {
            int max = remaining - (remainingCount - 1);
            int amount = ThreadLocalRandom.current().nextInt(1, max + 1);
            packets.add(amount);
            remaining -= amount;
            remainingCount--;
        }
        packets.add(remaining);
        Collections.shuffle(packets);
    }

    public synchronized Integer grab() {
        if (packets.isEmpty()) {
            return null;
        }
        return packets.remove(0);
    }
}
