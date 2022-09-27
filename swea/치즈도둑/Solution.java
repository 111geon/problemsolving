package 치즈도둑;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int n, ans;
  private static int[][] cheese;
  private static boolean[][] visited;
  private static final int[] dx = new int[]{-1, 0, 1, 0};
  private static final int[] dy = new int[]{0, 1, 0, -1};

  public static void main(String[] args) throws NumberFormatException, IOException {
    StringBuilder sb = new StringBuilder();
    int tc = Integer.parseInt(br.readLine());

    for (int t = 1; t <= tc; t++) {
      n = Integer.parseInt(br.readLine());
      cheese = new int[n][n];
      for (int i = 0; i < n; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int j = 0; j < n; j++) {
          cheese[i][j] = Integer.parseInt(st.nextToken());
        }
      }

      ans = 1;
      for (int i = 1; i < 100; i++) {
        ans = Math.max(ans, search(i));
      }

      sb.append("#" + t + " " + ans + System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static int search(int day) {
    visited = new boolean[n][n];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (cheese[i][j] <= day) {
          visited[i][j] = true;
        }
      }
    }

    int chunk = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (visited[i][j]) continue;
        chunk++;

        List<int[]> stack = new ArrayList<>();
        stack.add(new int[]{i, j});
        while (!stack.isEmpty()) {
          int[] curr = stack.remove(stack.size()-1);
          int x = curr[0], y = curr[1];
          visited[x][y] = true;
          
          for (int k = 0; k < 4; k++) {
            int nx = x + dx[k], ny = y + dy[k];
            if (nx >= n || ny >= n || nx < 0 || ny < 0) continue;
            if (visited[nx][ny]) continue;
            stack.add(new int[]{nx, ny});
          }
        }
      }
    }

    return chunk;
  }
}
