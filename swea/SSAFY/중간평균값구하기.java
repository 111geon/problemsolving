package swea.SSAFY;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 중간평균값구하기 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        int ntc = sc.nextInt();
        for (int tc=1; tc<=ntc; tc++) {
            List<Integer> nums = new ArrayList<>();
            
            for (int i=0; i<10; i++) {
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

            int sumNums = 0;
            for (int i=1; i<9; i++) {
                sumNums += nums.get(i);
            }

            System.out.println("#" + tc + " " + Math.round(sumNums/8.0));

        }
    }
}
