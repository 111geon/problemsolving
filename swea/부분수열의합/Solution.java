package 부분수열의합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n, k, ans;
    private static List<Integer> A;

    public static void main(String[] args) throws NumberFormatException, IOException {
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            A = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                A.add(Integer.parseInt(st.nextToken()));
            }

            ans = 0;
            solve(0, 0, 0);
            sb.append("#" + t + " " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static void solve(int start, int sum, int v) {
        if (sum == k) {
            ans++;
            return;
        }
        if (start == n || sum > k) {
            return;
        }
        for (int i = start; i < n; i++) {
            if ((v & 1 << i) != 0) continue;

            sum += A.get(i);
            solve(i+1, sum, v | 1 << i);
            sum -= A.get(i);
        }
    }
}
