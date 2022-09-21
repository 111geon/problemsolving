package 원재의메모리복구하기;

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
            String memory = br.readLine();
            int ans = 0;
            char curr = '0';
            for (int i = 0; i < memory.length(); i++) {
                if (memory.charAt(i) == curr) continue;
                ans++;
                curr = curr == '0' ? '1' : '0';
            }
            sb.append(" " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}
