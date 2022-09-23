package 디저트카페;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int n, ans;
  private static int[][] deserts;
  private static int[] dx = new int[]{1, 1, -1, -1};
  private static int[] dy = new int[]{-1, 1, 1, -1};
  private static boolean[] visited;

  public static void main(String[] args) throws NumberFormatException, IOException {
    StringBuilder sb = new StringBuilder();
    int tc = Integer.parseInt(br.readLine());
    for (int t = 1; t <= tc; t++) {
      n = Integer.parseInt(br.readLine());
      deserts = new int[n][n];
      for (int i = 0; i < n; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int j = 0; j < n; j++) {
          deserts[i][j] = Integer.parseInt(st.nextToken());
        }
      }

      ans = 0;
      visited = new boolean[101];
      for (int i = 0; i < n-2; i++) {
        for (int j = 1; j < n-1; j++) {
          solve(i, j, new int[]{0, 0, 0, 0}, 0);
        }
      }
      sb.append("#" + t + " " + (ans == 0 ? -1 : ans) + System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static void solve(int x, int y, int[] l, int d) {
    if (d == 3 && l[1] == l[3]) {
      ans = Math.max(ans, l[0] + l[1] + l[2] + l[3]);
      return;
    }
    if (y < 0 || x < 0 || x >= n || y >= n || visited[deserts[x][y]]) return;
    if (d == 2 && l[2] > l[0]) return;
    if (d == 3 && l[0] != l[2]) return;
    if (d > 3) return;

    visited[deserts[x][y]] = true;
    l[d]++;
    int nx = x + dx[d], ny = y + dy[d];
    solve(nx, ny, l, d);
    solve(nx, ny, l, d+1);
    l[d]--;
    visited[deserts[x][y]] = false;
  }
}