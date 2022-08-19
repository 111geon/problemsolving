package swea.SSAFY;

import java.util.Scanner;

public class 최빈수구하기 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        int ntc = sc.nextInt();

        for (int tc=1; tc<=ntc; tc++) {
            sc.nextInt();
            int[] scores = new int[101];

            for (int i=0; i<1000; i++) {
                scores[sc.nextInt()] += 1;
            }

            int maxVal = 0;
            int ans = 0 ;

            for (int i=0; i<101; i++) {
                if (scores[i] >= maxVal) {
                    maxVal = scores[i];
                    ans = i;
                }
            }

            System.out.println("#" + tc + " " + ans);
        }
    }
}
