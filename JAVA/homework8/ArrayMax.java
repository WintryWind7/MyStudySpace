package homework8;

public class ArrayMax {
    public static void main(String[] args) {
        int[] array = {5, 12, 3, 8, 20, 1, 15};
        try {
            int max = findMax(array);
            System.out.println("数组中的最大值是: " + max);
        } catch (IllegalArgumentException e) {
            System.out.println("错误: " + e.getMessage());
        }
        
        int[] emptyArray = {};
        try {
            int max2 = findMax(emptyArray);
            System.out.println("数组中的最大值是: " + max2);
        } catch (IllegalArgumentException e) {
            System.out.println("错误: " + e.getMessage());
        }
        
        int[] nullArray = null;
        try {
            int max3 = findMax(nullArray);
            System.out.println("数组中的最大值是: " + max3);
        } catch (IllegalArgumentException e) {
            System.out.println("错误: " + e.getMessage());
        }
    }
    
    public static int findMax(int[] array) {
        if (array == null) {
            throw new IllegalArgumentException("数组不能为null");
        }
        
        if (array.length == 0) {
            throw new IllegalArgumentException("数组不能为空");
        }
        
        int max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }
        
        return max;
    }
}

