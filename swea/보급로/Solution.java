package 보급로;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
   
public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, ans, nx, ny;
    static byte[][] matrix;
    static int[][] dp;
    static final int[] dx = new int[]{-1, 0, 1, 0};
    static final int[] dy = new int[]{0, 1, 0, -1};
    static PriorityQueue<int[]> q;
    static boolean[][] visited;
   
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            int n = Integer.parseInt(br.readLine());
            matrix = new byte[n][n];
            for (int i = 0; i < n; i++) {
                char[] row = br.readLine().toCharArray();
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = (byte)(row[j] - '0');
                }
            }
 
            visited = new boolean[n][n];
            dp = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dp[i][j] = Integer.MAX_VALUE;
                }
            }
            dp[0][0] = 0;
            q = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
            q.add(new int[]{0, 0, 0});
 
            while (!q.isEmpty()) {
                int[] curr = q.poll();
                int cost = curr[0], x = curr[1], y = curr[2];
                if (visited[x][y]) continue;
                visited[x][y] = true;
                if (x == n - 1 && y == n - 1) break;
                for (int i = 0; i < 4; i++) {
                    nx = x + dx[i];
                    ny = y + dy[i];
                    if (nx >= n || ny >= n || nx < 0 || ny < 0 || visited[nx][ny] || dp[nx][ny] <= cost + matrix[nx][ny]) continue;
                    dp[nx][ny] = cost + matrix[nx][ny];
                    q.add(new int[]{dp[nx][ny], nx, ny});
                }
            }
 
            ans = dp[n-1][n-1];
            sb.append("#" + t + " " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}
