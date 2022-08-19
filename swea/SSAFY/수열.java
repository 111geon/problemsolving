package ps;

import java.util.Scanner;

public class 수열 {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] nums = new int[n];

        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        int temp = 0;
        for (int i = 0; i < k; i++) {
            temp += nums[i];
        }

        int ans = temp;
        for (int i = 0; i < n - k; i++) {
            temp -= nums[i];
            temp += nums[i+k];
            ans = Math.max(ans, temp);            
        }

        System.out.println(ans);
    }
}
