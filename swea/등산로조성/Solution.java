package 등산로조성;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int n, k, ans;
  private static int[][] heights;
  private static boolean[][] visited;
  private static final int[] dx = new int[]{-1, 0, 1, 0};
  private static final int[] dy = new int[]{0, 1, 0, -1};

  public static void main(String[] args) throws NumberFormatException, IOException {
    StringBuilder sb = new StringBuilder();
    int tc = Integer.parseInt(br.readLine());

    for (int t = 1; t <= tc; t++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      k = Integer.parseInt(st.nextToken());

      heights = new int[n][n];
      for (int i = 0; i < n; i++) {
        st = new StringTokenizer(br.readLine());
        for (int j = 0; j < n; j++) {
          heights[i][j] = Integer.parseInt(st.nextToken());
        }
      }

      int maxHeight = 0;
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
          if (heights[i][j] > maxHeight) maxHeight = heights[i][j];
        }
      }

      ans = 0;
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
          if (heights[i][j] == maxHeight) {
            visited = new boolean[n][n];
            visited[i][j] = true;
            search(i, j, 1, false);
          }
        }
      }

      sb.append("#" + t + " " + ans + System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static void search(int x, int y, int length, boolean isDug) {
    if (length > ans) ans = length;
    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i], ny = y + dy[i];
      if (nx >= n || ny >= n || nx < 0 || ny < 0) continue;
      if (visited[nx][ny]) continue;
      if (heights[nx][ny] >= heights[x][y]) {
        if (isDug) continue;
        if (heights[nx][ny] - heights[x][y] >= k) continue;
        int temp = heights[nx][ny];

        heights[nx][ny] = heights[x][y] - 1;
        visited[nx][ny] = true;
        search(nx, ny, length+1, true);
        visited[nx][ny] = false;
        heights[nx][ny] = temp;

      } else {
        visited[nx][ny] = true;
        search(nx, ny, length+1, isDug);
        visited[nx][ny] = false;
      }
    }
  }
}
