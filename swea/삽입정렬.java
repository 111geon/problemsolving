package ps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 삽입정렬 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for (int t = 1; t <= tc; t++) {
            StringBuffer sb = new StringBuffer();
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            int temp;
            for (int i = 1; i < n; i++) {
                for (int j = i; j > 0; j--) {
                    if (arr[j] >= arr[j-1]) break;
                    temp = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = temp;
                }
            }

            for (int element: arr) {
                sb.append(element + " ");
            }
            sb.delete(sb.length()-1, sb.length());
            System.out.println("#" + t + " " + sb.toString());
        }
    }
}
