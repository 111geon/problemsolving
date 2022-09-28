package 장훈이의높은선반;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int n, b;
  private static int[] h;

  public static void main(String[] args) throws NumberFormatException, IOException {
    StringBuilder sb = new StringBuilder();
    int tc = Integer.parseInt(br.readLine());
    for (int t = 1; t <= tc; t++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      b = Integer.parseInt(st.nextToken());
      st = new StringTokenizer(br.readLine());
      h = new int[n];
      for (int i = 0; i < n; i++) {
        h[i] = Integer.parseInt(st.nextToken());
      }

      int[] ans = new int[]{Integer.MAX_VALUE};
      comb(0, 0, ans);

      sb.append("#" + t + " " + ans[0] + System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static void comb(int idx, int sum, int[] ans) {
    if (sum >= b) {
      ans[0] = Math.min(ans[0], sum - b);
      return;
    }
    if (sum - b > ans[0]) return;
    if (idx >= n) return;
    comb(idx+1, sum + h[idx], ans);
    comb(idx+1, sum, ans);
  }
}