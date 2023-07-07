import java.util.ArrayList;
import java.util.List;

public class SubarrayMinimum {
    public static List<Integer> findMinimums(int[] nums, int n, int s) {
        List<Integer> minimums = new ArrayList<>();

        for (int i = 0; i <= nums.length - n; i += s) {
            int min = Integer.MAX_VALUE;

            for (int j = i; j < i + n; j++) {
                if (nums[j] < min) {
                    min = nums[j];
                }
            }

            minimums.add(min);
        }

        return minimums;
    }

    public static void main(String[] args) {
        int[] nums = {4, 7, 3, 9, 6, 1, 8, 0};
        int n = 3;
        int s = 1;

        int[] nums2 = {4, 7, 3, 9, 6, 1, 8, 0};
        int n2 =2;
        int s2 =2;

        List<Integer> minimums = findMinimums(nums, n, s);
        System.out.println(minimums); // Output: [3, 3, 3, 1, 1, 0]
        List<Integer> minimums2 = findMinimums(nums2, n2, s2);
        System.out.println(minimums2); 
    }
}
