package ps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 퍼펙트셔플 {
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int tc = Integer.parseInt(br.readLine());
    for (int t = 1; t <= tc; t++) {
      StringBuffer sb = new StringBuffer();
      sb.append("#" + t + " ");

      int n = Integer.parseInt(br.readLine());
      String[] strArr = br.readLine().split(" ");

      int mid = (n + 1) / 2;
      int i = 0, j = mid;
      for (; i < mid - 1;) {
        sb.append(strArr[i++] + " ");
        sb.append(strArr[j++] + " ");
      }
      sb.append(strArr[i] + " ");
      if (n % 2 == 0) sb.append(strArr[j] + " ");

      sb.delete(sb.length()-1, sb.length());
      System.out.println(sb.toString());

    }
  }
}
