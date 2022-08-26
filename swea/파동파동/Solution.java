package ps.파동파동;

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
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            for (int i = 0; i < n; i++) {
                int temp = 0;
                for (int j = 0; j < n; j++) {
                    int val = Math.max(0, m + d * Math.max(Math.abs(i-r+1), Math.abs(j-c+1)));
                    temp += Math.min(val, 255);
                }
                sb.append(" " + temp);
            }
            sb.append(System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}
