package 폭탄뭐시기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            int[][] score = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    score[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int ans = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    ans = Math.max(ans, bombCross(score, n, p, i, j));
                    ans = Math.max(ans, bombX(score, n, p, i, j));
                }
            }

            sb.append("#" + t + " " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static int bombCross(int[][] score, int n, int p, int x, int y) {
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        return bomb(score, n, p, x, y, dx, dy);
    }
    
    private static int bombX(int[][] score, int n, int p, int x, int y) {
        int[] dx = {1, 1, -1, -1};
        int[] dy = {1, -1, 1, -1};
        return bomb(score, n, p, x, y, dx, dy);
    }

    private static int bomb(int[][] score, int n, int p, int x, int y, int[] dx, int[] dy) {
        int ans = score[x][y];
        for (int i = 1; i <= p; i++) {
            for (int j = 0; j < dx.length; j++) {
                int nx = x + dx[j] * i;
                int ny = y + dy[j] * i;

                if (nx >= n || nx < 0 || ny >= n || ny < 0) continue;
                ans += score[nx][ny];
            }
        }
        return ans;
    }
}
