package N과M.N과M11;

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
  static boolean[] v;

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
    v = new boolean[n];
    solve(0);
    System.out.println(sb.toString());
  }

  private static void solve(int sidx) {
    if (sidx == m) {
      for (int e: s) {
        sb.append(e + " ");
      }
      sb.append(System.lineSeparator());
      return;
    }

    int t = 0;
    for (int i = 0; i < n; i++) {
      if (ls[i] == t) continue;
      s[sidx] = ls[i];
      t = ls[i];
      solve(sidx+1);
    }
  }
}
