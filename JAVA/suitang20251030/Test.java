package suitang20251030;

import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Manage manage = new Manage();
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("===================");
            System.out.println(" 1.小猫 2.小狗 0.退出");
            System.out.println("请选择:");
            int choice = scanner.nextInt();
            
            Animal animal = manage.select(choice);
            
            if (animal != null) {
                System.out.println(animal.eat());
            }
        }
    }
}
