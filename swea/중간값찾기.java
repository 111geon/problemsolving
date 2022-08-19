package swea.SSAFY;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 중간값찾기 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        int n = sc.nextInt();
        sc.nextLine();

        List<Integer> nums = new ArrayList<>();
        for (int i=0; i<n; i++) {
            int nextNum = sc.nextInt();
            int nextIdx = nums.size();

            for (int j=0; j<nums.size(); j++) {
                if (nums.get(j) > nextNum) {
                    nextIdx = j;
                    break;
                }
            }

            nums.add(nextIdx, nextNum);

        }

        System.out.println(nums.get(n/2));
    }
    
}
