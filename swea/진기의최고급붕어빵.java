package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 진기의최고급붕어빵 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int[] customers = new int[n];
            for (int i = 0; i < n; i++) {
                customers[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(customers);

            String ans = "Possible";
            for (int i = 0; i < n; i++) {
                if (k * (customers[i] / m) - (i) <= 0) {
                    ans = "Impossible";
                    break;
                }
            }

            System.out.println("#" + t + " " + ans);
        }
    }
}
