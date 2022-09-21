package 정곤이의단조증가하는수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            sb.append("#" + t);
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(a);

            sb.append(" " + maxAsc(n, a) + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static int maxAsc(int n, int[] a) {
        int max = -1;
        for (int i = n - 1; i > 0; i--) {
            for (int j = i - 1; j >= 0; j--) {
                if (isAsc(a[i] * a[j])) {
                    max = a[i] * a[j];
                    
                    for (int k = i - 1; k > j; k--) {
                        for (int l = k - 1; l >= j; l--) {
                            if (isAsc(a[k] * a[l])) {
                                max = Math.max(max, a[k] * a[l]);
                            }
                        }
                    }

                    return max;
                }
            }
        }
        return -1;
    }

    private static boolean isAsc(int num) {
        int temp = 10;
        while (num > 0) {
            if (num % 10 > temp) return false;
            temp = num % 10;
            num /= 10;
        }
        return true;
    }
}
