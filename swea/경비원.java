

import java.util.Scanner;

public class 경비원 {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int a = sc.nextInt();
        int b = sc.nextInt();
        int l = 2 * (a + b);

        int n = sc.nextInt();
        int[][] p = makePoints(a, b, n);
        int ans = 0;
        int temp;

        for (int i = 0; i < n; i++) {
            if ((p[i][0] == 0 && p[n][0] == a) || (p[i][0] == a && p[n][0] == 0)) {
                temp = a + p[i][1] + p[n][1];
                ans += Math.min(temp, l-temp);
            } else if ((p[i][1] == 0 && p[n][1] == b) || (p[i][1] == b && p[n][1] == 0)) {
                temp = b + p[i][0] + p[n][0];
                ans += Math.min(temp, l-temp);
            } else {
                ans += Math.abs(p[i][0] - p[n][0]) + Math.abs(p[i][1] - p[n][1]);
            }
        }

        System.out.println(ans);
    }

    private static int[][] makePoints(int a, int b, int n) {
        int[][] points = new int[n+1][2];
        int direction;
        for (int i = 0; i < n+1; i++) {
            direction = sc.nextInt();
            if (direction == 1) {
                points[i][0] = sc.nextInt();
                points[i][1] = b;
            } else if (direction == 2) {
                points[i][0] = sc.nextInt();
                points[i][1] = 0;
            } else if (direction == 3) {
                points[i][0] = 0;
                points[i][1] = b - sc.nextInt();
            } else {
                points[i][0] = a;
                points[i][1] = b - sc.nextInt();
            }
        }
        return points;
    }
}
