package 러시아국기같은깃발;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            sb.append("#" + t);
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int[][] req = new int[n][3]; // {for W, for B, for R}
            for (int i = 0; i < n; i++) {
                String row = br.readLine();
                int forW = m, forB = m, forR = m;
                for (int j = 0; j < m; j++) {
                    if (row.charAt(j) == 'W') forW--;
                    else if (row.charAt(j) == 'B') forB--;
                    else forR--;
                }
                req[i][0] = forW;
                req[i][1] = forB;
                req[i][2] = forR;
            }

            int ans = Integer.MAX_VALUE;
            for (int bTop = 1; bTop < n - 1; bTop++) {
                for (int bBot = bTop; bBot < n - 1; bBot++) {
                    int temp = 0;
                    for (int i = 0; i < n; i++) {
                        if (i < bTop) temp += req[i][0];
                        else if (bTop <= i && i <= bBot) temp += req[i][1];
                        else temp += req[i][2];
                    }
                    ans = Math.min(ans, temp);
                }
            }
            sb.append(" " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}
