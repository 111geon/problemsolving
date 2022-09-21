

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class 괄호짝짓기 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuffer sb = new StringBuffer();

    Map<Character, Character> map = new HashMap<>();
    map.put(')', '(');
    map.put(']', '[');
    map.put('}', '{');
    map.put('>', '<');

    for (int t = 1; t <= 10; t++) {
      sb.append("#" + t + " ");
      int n = Integer.parseInt(br.readLine());
      char[] arr = br.readLine().toCharArray();
      char[] stack = new char[n];
      int top = 0;

      for (int i = 0; i < n; i++) {
        if (!map.containsKey(arr[i])) {
          stack[top++] = arr[i];
        } else {
          if (stack[top-1] != map.get(arr[i])) {
            break;
          } else {
            top--;
          }
        }
      }

      if (top != 0) {
        sb.append(0 + System.lineSeparator());
      } else {
        sb.append(1 + System.lineSeparator());
      }

    }

    System.out.println(sb.toString());
  }
}
