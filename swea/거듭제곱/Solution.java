package 거듭제곱;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws NumberFormatException, IOException {
    StringBuilder sb = new StringBuilder();

    for (int t = 1; t <= 10; t++) {
      br.readLine();
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());

      int ans = pow(n, m, new HashMap<>());
      
      sb.append("#" + t + " " + ans + System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static int pow(int n, int m, Map<Integer, Integer> memo) {
    if (m == 0) return 1;
    if (m == 1) return n;
    int halfKey = m / 2;
    if (!memo.containsKey(halfKey)) {
      int halfVal = pow(n, halfKey, memo);
      memo.put(halfKey, halfVal * halfVal * (m % 2 == 1 ? n : 1));
    }
    return memo.get(halfKey);
  }
}
