package why.no2;

import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int[] nums = new int[10];
        Random random = new Random();
        
        for (int i = 0; i < nums.length; i++) {
            nums[i] = 10 + random.nextInt(90);
        }
        
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        
        System.out.print("生成的数组：");
        for (int num : nums) {
            System.out.print(num + " ");
        }
        System.out.println("\n最大值：" + max);
    }
}