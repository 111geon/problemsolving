package ps.숫자배열회전;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            sb.append("#" + t + System.lineSeparator());
            int n = Integer.parseInt(br.readLine());
            char[][] nums = new char[n][n];
            for (int i = 0; i < n; i++) {
                String row = br.readLine();
                for (int j = 0; j < n; j++) {
                    nums[i][j] = row.charAt(2 * j);
                }
            }

            for (int i = 0; i < n; i++) {
                char[] temp = new char[n];

                for (int j = 0; j < n; j++) {
                    temp[j] = nums[n-j-1][i];
                }
                sb.append(String.valueOf(temp) + " ");

                for (int j = 0; j < n; j++) {
                    temp[j] = nums[n-i-1][n-j-1];
                }
                sb.append(String.valueOf(temp) + " ");

                for (int j = 0; j < n; j++) {
                    temp[j] = nums[j][n-i-1];
                }
                sb.append(String.valueOf(temp) + System.lineSeparator());
            }
        }
        System.out.println(sb.toString());
    }
}
