package 보호필름;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int d, w, k, ans;
  private static char[][] film;

  public static void main(String[] args) throws NumberFormatException, IOException {
    StringBuilder sb = new StringBuilder();
    int tc = Integer.parseInt(br.readLine());
    for (int t = 1; t <= tc; t++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      d = Integer.parseInt(st.nextToken());
      w = Integer.parseInt(st.nextToken());
      k = Integer.parseInt(st.nextToken());
      film = new char[d][w];
      for (int i = 0; i < d; i++) {
        st = new StringTokenizer(br.readLine());
        for (int j = 0; j < w; j++) {
          film[i][j] = st.nextToken().charAt(0);
        }
      }
      ans = k;
      solve(0, 0);
      sb.append("#" + t + " " + ans + System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static void solve(int depth, int start) {
    if (depth >= ans) return;
    if (check(film)) {
      ans = Math.min(ans, depth);
      return;
    }
    for (int i = start; i < d; i++) {
      char[] savedRow = Arrays.copyOf(film[i], w);
      changeRow(i, '0');
      solve(depth+1, i+1);
      changeRow(i, '1');
      solve(depth+1, i+1);
      film[i] = savedRow;
    }
  }

  private static void changeRow(int i, char toChange) {
    for (int j = 0; j < w; j++) {
      film[i][j] = toChange;
    }
  }

  private static boolean check(char[][] film) {
    for (int i = 0; i < w; i++) {
      int cnt = 1;
      char prev = film[0][i];
      boolean isChecked = false;

      for (int j = 1; j < d; j++) {
        if (film[j][i] == prev) {
          cnt++;
        } else {
          cnt = 1;
          prev = film[j][i];
        }

        if (cnt >= k) {
          isChecked = true;
          break;
        }
      }
      if (!isChecked) return false;
    }
    return true;
  }
}
