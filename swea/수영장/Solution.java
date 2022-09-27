package 수영장;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int d, m, m3, y, ans;
    private static int[] plan;
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            d = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            m3 = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            plan = new int[13];
            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= 12; i++) {
                plan[i] = Integer.parseInt(st.nextToken());
            }

            ans = y;
            dfs(1, 0);
            sb.append("#" + t + " " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static void dfs(int start, int sum) {
        if (start >= 13) {
            ans = Math.min(ans, sum);
            return;
        }
        dfs(start+3, sum + m3);
        dfs(start+1, sum + m);
        dfs(start+1, sum + d * plan[start]);
    }
}
