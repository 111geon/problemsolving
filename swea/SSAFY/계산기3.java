package ps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class 계산기3 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuffer sb = new StringBuffer();
    List<Character> charStack = new ArrayList<>();
    List<Integer> intStack = new ArrayList<>();

    for (int t = 1; t <= 10; t++) {
      int n = Integer.parseInt(br.readLine());
      String str = br.readLine();
      char curr;

      // 후위표현식으로 변환
      for (int i = 0; i < n; i++) {
        curr = str.charAt(i);
        if (curr == '(' || curr == '*') {
          charStack.add(curr);
        } else if (curr == '+') {
          while (!charStack.isEmpty() && charStack.get(charStack.size()-1) != '(') {
            sb.append(charStack.remove(charStack.size()-1));
          }
          charStack.add(curr);
        } else if (curr == ')') {
          while (charStack.get(charStack.size()-1) != '(') {      
            sb.append(charStack.remove(charStack.size()-1));
          }
          charStack.remove(charStack.size()-1);
        } else {
          sb.append(curr);
        }
      }
      while (!charStack.isEmpty()) sb.append(charStack.remove(charStack.size()-1));
      str = sb.toString();

      // 후위표현식 계산
      n = str.length();
      for (int i = 0; i < n; i++) {
        curr = str.charAt(i);
        if (curr == '+') {
          intStack.add(intStack.remove(intStack.size()-1) + intStack.remove(intStack.size()-1));
        } else if (curr == '*') {
          intStack.add(intStack.remove(intStack.size()-1) * intStack.remove(intStack.size()-1));
        } else {
          intStack.add(curr - '0');
        }
      }

      System.out.println("#" + t + " " + intStack.remove(intStack.size()-1));
    }
  }
}
