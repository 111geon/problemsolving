package swea.SSAFY;

import java.util.Scanner;

public class Sum {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        int n = 100;
        for (int t = 1; t <= 10; t++) {
            int tc = sc.nextInt();
            int[][] mat = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    mat[i][j] = sc.nextInt();
                }
            }

            int maxVal = 0;
            int temp;

            for (int i = 0; i < n; i++) {
                temp = 0;
                for (int j = 0; j < n; j++) {
                    temp += mat[i][j];
                }
                maxVal = Math.max(maxVal, temp);

                temp = 0;
                for (int j = 0; j < n; j++) {
                    temp += mat[j][i];
                }
                maxVal = Math.max(maxVal, temp);
            }

            temp = 0;
            for (int i = 0; i < n; i++) {
                temp += mat[i][i];
            }
            maxVal = Math.max(maxVal, temp);

            temp = 0;
            for (int i = 0; i < n; i++) {
                temp += mat[i][n-i-1];
            }
            maxVal = Math.max(maxVal, temp);

            System.out.println("#" + tc + " " + maxVal);
        }
    }
}
