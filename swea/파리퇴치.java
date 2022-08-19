package swea.SSAFY;

import java.util.Scanner;

public class 파리퇴치 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        int tc = sc.nextInt();
        for (int t=1; t<=tc; t++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] mat = new int[n][n];
            for (int i=0; i<n; i++) {
                for (int j=0; j<n; j++) {
                    mat[i][j] = sc.nextInt();
                }
            }

            int ans = 0;
            int temp;
            for (int i = 0; i <= n - m; i++) {
                for (int j = 0; j <= n - m; j++) {
                    temp = 0;
                    for (int k = 0; k < m; k++) {
                        for (int l = 0; l < m; l++) {
                            temp += mat[i+k][j+l];
                        }
                    }
                    ans = Math.max(ans, temp);
                }
            }

            System.out.println("#" + t + " " + ans);

        }
    
    }
}
