package homework7;

interface USB {
    void start();
    void stop();
}

class Phone implements USB {
    public void start() {
    }
    
    public void stop() {
    }
}

class Camera implements USB {
    public void start() {
    }
    
    public void stop() {
    }
}

public class Computer {
    public void useUSB(USB device) {
        device.start();
        device.stop();
    }
    
    public static void main(String[] args) {
        Computer computer = new Computer();
        
        USB phone = new Phone();
        USB camera = new Camera();
        
        computer.useUSB(phone);
        
        computer.useUSB(camera);
    }
}
