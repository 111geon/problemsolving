package swea.SSAFY;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 쇠막대기 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int tc = Integer.parseInt(br.readLine());

    for (int t = 1; t <= tc; t++) {
      StringBuffer sb = new StringBuffer();
      sb.append("#" + t + " ");

      char[] arr = br.readLine().toCharArray();
      int ans = 0, stack = 0;
      for (int i = 0; i < arr.length; i++) {
        if (arr[i] == '(') {
          if (arr[i+1] == ')') {
            ans += stack;
            i++;
          } else {
            stack++;
          }
        } else {
          ans++;
          stack--;
        }
      }

      sb.append(ans);
      System.out.println(sb.toString());
    }
  }
}
