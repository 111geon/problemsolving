package 규영이와인영이의카드게임;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static StringBuilder sb = new StringBuilder();
  private static int n = 18, m = 9;
  private static List<Integer> cardsA, cardsB;
  private static Map<Integer, Integer> fact = new HashMap<>();

  public static void main(String[] args) throws NumberFormatException, IOException {
    int T = Integer.parseInt(br.readLine());
    for (int t = 1; t <= T; t++) {

      cardsA = new ArrayList<>();
      cardsB = new ArrayList<>();

      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int i = 0; i < m; i ++) {
        cardsA.add(Integer.parseInt(st.nextToken()));
      }
      for (int i = 1; i <= n; i++) {
        if (!cardsA.contains(i)) cardsB.add(i);
      }

      int[] ans = new int[1];
      solve(0, 0, new boolean[m], ans);
      sb.append("#" + t + " " + ans[0] + " " + (362880 - ans[0]) + System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static void solve(int sidx, int score, boolean[] v, int[] ans) {
    if (score > 85) {
      ans[0] += factorial(m-sidx);
      return;
    }
    if (sidx == m) return;

    for (int i = 0; i < m; i++) {
      if (v[i]) continue;

      int win = 0;
      if (cardsA.get(sidx) > cardsB.get(i)) {
        win = cardsA.get(sidx) + cardsB.get(i);
      }

      score += win;
      v[i] = true;
      solve(sidx+1, score, v, ans);
      v[i] = false;
      score -= win;
    }
  }

  private static int factorial(int n) {
    if (n == 0) return 1;
    if (!fact.containsKey(n)) fact.put(n, n * factorial(n-1));
    return fact.get(n);
  }
}
