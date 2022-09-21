

import java.util.Scanner;

public class 달팽이숫자 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        int t = sc.nextInt();
        for (int tc = 1; tc <= t; tc++) {
            System.out.println("#" + tc);
            int n = sc.nextInt();
            int[][] snail = new int[n][n];

            int x = 0, y = 0, i = 1;
            while (i <= n * n) {
                while (y < n && snail[x][y] == 0) {
                    snail[x][y] = i++;
                    y++;
                }
                y--;
                x++;

                while (x < n && snail[x][y] == 0) {
                    snail[x][y] = i++;
                    x++;
                }
                x--;
                y--;


                while (y >= 0 && snail[x][y] == 0) {
                    snail[x][y] = i++;
                    y--;
                }
                y++;
                x--;

                while (x >= 0 && snail[x][y] == 0) {
                    snail[x][y] = i++;
                    x--;
                }
                x++;
                y++;
            }

            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    System.out.print(snail[j][k] + " ");
                }
                System.out.println();
            }
        }
    }
}
