package suitang20251030;

public class Manage {
    public Animal select(int key) {
        Animal animal = null;
        switch (key) {
            case 1:
                animal = new Cat();
                break;
            case 2:
                animal = new Dog();
                break;
            case 0:
                System.out.println("程序已退出");
                System.exit(0);
        }
        return animal;
    }
}
