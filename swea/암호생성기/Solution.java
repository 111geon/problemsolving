package ps.day0825.암호생성기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        for (int t = 1; t <= 10; t++) {
            sb.append("#" + t);
            br.readLine();
            StringTokenizer st = new StringTokenizer(br.readLine());
            Deque<Integer> deque = new ArrayDeque<>();
            for (int i = 0; i < 8; i++) deque.addLast(Integer.parseInt(st.nextToken()));

            encrypt(deque);

            for (int i = 0; i < 8; i++) sb.append(" " + deque.pollFirst());
            sb.append(System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static void encrypt(Deque<Integer> deque) {
        while (true) {
            for (int i = 1; i <= 5; i++) {
                int temp = deque.pollFirst();
                temp = Math.max(0, temp-i);
                deque.addLast(temp);
                if (temp == 0) return;
            }
        }
    }
}
