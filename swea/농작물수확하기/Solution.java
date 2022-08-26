package ps.농작물수확하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            int n = Integer.parseInt(br.readLine());
            int ans = 0;
            for (int i = 0; i < n / 2; i++) {
                String row = br.readLine();
                for (int j = n / 2 - i; j <= n / 2 + i; j++) {
                    ans += row.charAt(j) - '0';
                }
            }
            for (int i = n / 2; i < n; i++) {
                String row = br.readLine();
                for (int j = i - n / 2; j < n + n / 2 - i; j++) {
                    ans += row.charAt(j) - '0';
                }
            }
            sb.append("#").append(t).append(" ").append(ans).append(System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}
