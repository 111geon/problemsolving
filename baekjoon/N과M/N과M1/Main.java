package N과M.N과M1;

import java.util.Scanner;

public class Main {
  static Scanner sc = new Scanner(System.in);
  static StringBuilder sb = new StringBuilder();
  static int n, m;
  static int[] s;
  static boolean[] v;

  public static void main(String[] args) {
    n = sc.nextInt();
    m = sc.nextInt();
    s = new int[m];
    v = new boolean[n+1];
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
    for (int i = 1; i <= n; i++) {
      if (v[i]) continue;
      s[sidx] = i;
      v[i] = true;
      solve(sidx+1);
      v[i] = false;
    }
  }
}
