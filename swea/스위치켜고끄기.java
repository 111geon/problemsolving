package ps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 스위치켜고끄기 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] switches = new int[n];
        for (int i = 0; i < n; i++) {
            switches[i] = Integer.parseInt(st.nextToken());
        }
        
        int m = Integer.parseInt(br.readLine());
        int gender, s;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            gender = Integer.parseInt(st.nextToken());
            s = Integer.parseInt(st.nextToken());

            if (gender == 1) {
                for (int j = 1; j * s - 1 < n; j++) {
                    switches[j*s-1] = (switches[j*s-1] + 1) % 2;
                }
            } else {
                switches[s-1] = (switches[s-1] + 1) % 2;
                int j = 1;
                while (s-j-1 >= 0 && s+j-1 < n) {
                    if (switches[s-j-1] != switches[s+j-1]) break;
                    switches[s-j-1] = (switches[s-j-1] + 1) % 2;
                    switches[s+j-1] = (switches[s+j-1] + 1) % 2;
                    j++;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            sb.append(switches[i] + " ");
            if ((i + 1) % 20 == 0) {
                sb.delete(sb.length()-1, sb.length());
                System.out.println(sb.toString());
                sb.setLength(0);
            }
        }
        if (sb.length() != 0) {
            sb.delete(sb.length()-1, sb.length());
            System.out.println(sb.toString());
        }
    }
}
