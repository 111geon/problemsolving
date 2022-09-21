package 연속된1의개수중최대값구하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            sb.append("#" + t);
            int n = Integer.parseInt(br.readLine());
            char[] chars = br.readLine().trim().toCharArray();

            int ans = 0, temp = 0;
            for (int i = 0; i < n; i++) {
                if (chars[i] == '1') {
                    temp++;
                    ans = Math.max(ans, temp);
                } else {
                    temp = 0;
                }
            }

            sb.append(" " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}
