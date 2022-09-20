package 요리사;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int n, m;
  private static int[][] score;

  public static void main(String[] args) throws NumberFormatException, IOException {
    int T = Integer.parseInt(br.readLine());
    for (int t = 1; t <= T; t++) {
      n = Integer.parseInt(br.readLine());
      m = n / 2;
      score = new int[n][n];
      for (int i = 0; i < n; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int j = 0; j < n; j++) {
          score[i][j] = Integer.parseInt(st.nextToken());
        }
      }

      int[] s = new int[m];
      int ans = solve(s, 1, 1, Integer.MAX_VALUE);
      System.out.println("#" + String.valueOf(t) + " " + String.valueOf(ans));
    }
  }

  private static int solve(int[] s, int sidx, int idx, int ans) {
    if (sidx == m) {
      int[] ss = new int[m];
      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
          if (!contains(s, j) && !contains(ss, j)) {
            ss[i] = j;
            break;
          }
        }
      }

      return Math.abs(cook(s, 0) - cook(ss, 0));
    }

    for (int i = idx; i < n; i++) {
      s[sidx] = i;
      ans = Math.min(ans, solve(s, sidx+1, i+1, ans));
    }
    return ans;
  }

  private static boolean contains(int[] ls, int n) {
    for (int i = 0; i < ls.length; i++) {
      if (ls[i] == n) return true;
    }
    return false;
  }

  private static int cook(int[] s, int sidx) {
    int ans = 0;
    for (int i = 0; i < s.length; i++) {
      for (int j = i+1; j < s.length; j++) {
        ans += score[s[i]][s[j]] + score[s[j]][s[i]];
      }
    }
    return ans;
  }
}
