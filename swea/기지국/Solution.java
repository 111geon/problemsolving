package 기지국;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            int n = Integer.parseInt(br.readLine());
            char[][] map = new char[n][n];
            for (int i = 0; i < n; i++) {
                map[i] = br.readLine().trim().toCharArray();
            }

            int ans = 0;
            boolean[][] visited = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (map[i][j] == 'A') {
                        ans -= count(n, map, visited, i, j, 1);
                    } else if (map[i][j] == 'B') {
                        ans -= count(n, map, visited, i, j, 2);
                    } else if (map[i][j] == 'C') {
                        ans -= count(n, map, visited, i, j, 3);
                    } else if (map[i][j] == 'H') {
                        ans++;
                    }
                }
            }

            sb.append("#" + t + " " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static int count(int n, char[][] map, boolean[][] visited, int x, int y, int r) {
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        int count = 0;
        for (int i = 0; i < dx.length; i++) {
            for (int j = 1; j <= r; j++) {
                int nx = x + dx[i] * j;
                int ny = y + dy[i] * j;
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if (map[nx][ny] == 'H' && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    count++;
                }
            }
        }

        return count;
    }
}
