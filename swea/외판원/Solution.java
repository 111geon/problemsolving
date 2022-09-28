package 외판원;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int ans, n;
  private static int[][] graph, dp;

  public static void main(String[] args) throws NumberFormatException, IOException {
    StringBuilder sb = new StringBuilder();
    int tc = Integer.parseInt(br.readLine());

    for (int t = 1; t <= tc; t++) {
      n = Integer.parseInt(br.readLine());

      StringTokenizer st = new StringTokenizer(br.readLine());
      int[][] points = new int[n+2][2];
      for (int i = 0; i < n + 2; i++) {
        points[i][0] = Integer.parseInt(st.nextToken());
        points[i][1] = Integer.parseInt(st.nextToken());
      }

      graph = new int[n+2][n+2];
      for (int i = 0; i < n + 2; i++) {
        for (int j = i+1; j < n + 2; j++) {
          int dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
          graph[i][j] = dist;
          graph[j][i] = dist;
        }
      }

      dp = new int[n+2][1<<(n+2)];

      // ans = Integer.MAX_VALUE;
      // solve(0, 0, 0, 0);
      ans = solve(0, 0, 0);

      sb.append("#" + t + " " + ans + System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static int solve(int start, int depth, int visited) {
    if (dp[start][visited] != 0) return dp[start][visited];
    if (depth == n) return graph[start][1];

    dp[start][visited] = Integer.MAX_VALUE;
    for (int i = 2; i < n+2; i++) {
      if ((visited & 1 << i) > 0) continue;
      dp[start][visited] = Math.min(dp[start][visited], solve(i, depth+1, visited | 1 << i) + graph[start][i]);
    }
    return dp[start][visited];
  }

  private static void solve(int start, int depth, int visited, int score) {
    if (score > ans) return;
    if (depth == n) {
      score += graph[start][1];
      ans = Math.min(ans, score);
      return;
    }
    for (int i = 2; i < n+2; i++) {
      if ((visited & 1 << i) > 0) continue;
      score += graph[start][i];
      solve(i, depth+1, visited | 1 << i, score);
      score -= graph[start][i];
    }
  }
}
