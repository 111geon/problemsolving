package 규영이와인영이의카드게임;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws NumberFormatException, IOException {
    int T = Integer.parseInt(br.readLine());
    for (int t = 1; t <= T; t++) {

      List<Integer> cardsA = new ArrayList<>();

      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int i = 0; i < 9; i ++) {
        cardsA.add(Integer.parseInt(st.nextToken()));
      }

    }
  }
}
