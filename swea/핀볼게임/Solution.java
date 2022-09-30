package 핀볼게임;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;
   
public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, ans;
    static byte[][] matrix;
    static final int[] dx = new int[]{-1, 0, 1, 0};
    static final int[] dy = new int[]{0, 1, 0, -1};
    static Map<String, String> teleport;
   
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            int n = Integer.parseInt(br.readLine());
 
            matrix = new byte[n+2][n+2];
            for (int i = 0; i < n + 2; i++) {
                matrix[0][i] = 5;
                matrix[n+1][i] = 5;
                matrix[i][0] = 5;
                matrix[i][n+1] = 5;
            }
 
            List<List<String>> wormHole = new ArrayList<>();
            for (int i = 0; i <= 10; i++) wormHole.add(new ArrayList<>());
            for (int i = 1; i < n + 1; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 1; j < n + 1; j++) {
                    byte num = Byte.parseByte(st.nextToken());
                    matrix[i][j] = num;
                    if (num > 5) wormHole.get(num).add(i + " " + j);
                }
            }
             
            teleport = new HashMap<>();
            for (int i = 6; i <= 10; i++) {
                if (wormHole.get(i).isEmpty()) continue;
                teleport.put(wormHole.get(i).get(0), wormHole.get(i).get(1));
                teleport.put(wormHole.get(i).get(1), wormHole.get(i).get(0));
            }
             
            ans = 0;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (matrix[i][j] != 0) continue;
                    for (int k = 0; k < 4; k++) {
                        playYYG(i, j, k);
                    }
                }
            }
            sb.append("#" + t + " " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
 
    static void playYYG(int x, int y, int direction) {
        int startX = x, startY = y;
        int score = 0;
        while (true) {
            x += dx[direction];
            y += dy[direction];
            if ((x == startX && y == startY) || matrix[x][y] == -1) {
                ans = Math.max(ans, score);
                return;
            }
            if (matrix[x][y] == 0) continue;
            if (matrix[x][y] < 6) {
                score++;
                direction = changeDirection(matrix[x][y], direction);
            } else {
                String[] newXY = teleport.get(x + " " + y).split(" ");
                x = Integer.parseInt(newXY[0]);
                y = Integer.parseInt(newXY[1]);
            }
        }
    }
 
    static int changeDirection(int shape, int direction) {
        int reverseDirection = (direction + 2) % 4;
        if (shape == 5) return reverseDirection;
        if (shape == 1) {
            if (direction == 0 || direction == 1) return reverseDirection;
            if (direction == 2) return 1;
            return 0;
        }
        if (shape == 2) {
            if (direction == 2 || direction == 1) return reverseDirection;
            if (direction == 0) return 1;
            return 2;
        }
        if (shape == 3) {
            if (direction == 2 || direction == 3) return reverseDirection;
            if (direction == 0) return 3;
            return 2;
        }
        if (shape == 4) {
            if (direction == 0 || direction == 3) return reverseDirection;
            if (direction == 1) return 0;
            return 3;
        }
        return -1;
    }
}
