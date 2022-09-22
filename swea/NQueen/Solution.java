package NQueen;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int n, ans;

  public static void main(String[] args) throws NumberFormatException, IOException {
    int tc = Integer.parseInt(br.readLine());
    StringBuilder sb = new StringBuilder();
    for (int t = 1; t <= tc; t++) {
      n = Integer.parseInt(br.readLine());
      ans = 0;
      nqueen(0, 0, 0, 0);
      sb.append("#" + t + " " + ans + System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static void nqueen(int idx, int vCol, int vDiag1, int vDiag2) {
    if (idx == n) {
      ans++;
      return;
    }

    for (int i = 0; i < n; i++) {
      if ((vCol & 1 << i) > 0 || 
          (vDiag1 & 1 << (idx + i)) > 0 ||
          (vDiag2 & 1 << (idx - i + (n - 1))) > 0
      ) continue;

      vCol = vCol | 1 << i;
      vDiag1 = vDiag1 | 1 << (idx + i);
      vDiag2 = vDiag2 | 1 << (idx - i + (n - 1));
      nqueen(idx+1, vCol, vDiag1, vDiag2);
      vCol = vCol ^ 1 << i;
      vDiag1 = vDiag1 ^ 1 << (idx + i);
      vDiag2 = vDiag2 ^ 1 << (idx - i + (n - 1));
    }
  }
}
