package N과M.N과M6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int n, m;
  static int[] s;
  static int[] ls;

  public static void main(String[] args) throws IOException {
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    st = new StringTokenizer(br.readLine());
    ls = new int[n];
    for (int i = 0; i < n; i++) {
      ls[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(ls);

    s = new int[m];
    solve(0, 0);
    System.out.println(sb.toString());
  }

  private static void solve(int sidx, int idx) {
    if (sidx == m) {
      for (int e: s) {
        sb.append(e + " ");
      }
      sb.append(System.lineSeparator());
      return;
    }
    for (int i = idx; i < n; i++) {
      s[sidx] = ls[i];
      solve(sidx+1, i+1);
    }
  }
}
