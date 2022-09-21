package 햄버거다이어트;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, limit, ans;
    static int[] scores, calories;

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            sb.append("#" + t + " ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            limit = Integer.parseInt(st.nextToken());

            scores = new int[n];
            calories = new int[n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                scores[i] = Integer.parseInt(st.nextToken());
                calories[i] = Integer.parseInt(st.nextToken());
            }

            int start = 0, sumCal = 0, sumSco = 0;
            dfs(start, sumCal, sumSco);
            sb.append(ans + System.lineSeparator());
            ans = 0;
        }
        System.out.println(sb.toString());
    }

    private static void dfs(int start, int sumCal, int sumSco) {
        ans = Math.max(sumSco, ans);
        for (int i = start; i < n; i++) {
            if (sumCal + calories[i] <= limit) {
                sumCal += calories[i];
                sumSco += scores[i];
                dfs(i+1, sumCal, sumSco);
                sumCal -= calories[i];
                sumSco -= scores[i];
            }
        }
    }

    // private static void dfs(int start, int sumCal, int sumSco) {
    //     if (sumCal > limit) return;
    //     if (start >= n) {
    //         ans = Math.max(sumSco, ans);
    //         return;
    //     }
    //     dfs(start+1, sumCal + calories[start], sumSco + scores[start]);
    //     dfs(start+1, sumCal, sumSco);
    // }

    // nC0 + nC1 + ... + nCn = 2^n
    // for문과 재귀를 이용해 조합 만들기 == 재귀로 모든 경우의 수(2^n)를 만들고 조합으로 백트래킹
}
