package 백만장자프로젝트;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            sb.append("#" + t);
            int n = Integer.parseInt(br.readLine());
            int[] prices = new int[n];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                prices[i] = Integer.parseInt(st.nextToken());
            }

            long ans = 0;
            int max = prices[n-1];
            for (int i = n - 1; i >= 0; i--) {
                max = Math.max(max, prices[i]);
                ans += max - prices[i];
            }

            sb.append(" " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}
