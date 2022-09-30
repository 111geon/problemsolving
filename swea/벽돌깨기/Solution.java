package 벽돌깨기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
   
public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, w, h, ans;
    static byte[][] matrix;
    static final int[] dx = new int[]{-1, 0, 1, 0};
    static final int[] dy = new int[]{0, 1, 0, -1};
   
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            matrix = new byte[h][w];
            for (int i = 0; i < h; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < w; j++) {
                    matrix[i][j] = Byte.parseByte(st.nextToken());
                }
            }
             
            ans = Integer.MAX_VALUE;
            play(0);
 
            sb.append("#" + t + " " + (ans) + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
 
    static void play(int depth) {
        if (depth == n) {
            ans = Math.min(ans, countMatrix());
            return;
        }
        for (int i = 0; i < w; i++) {
            byte[][] temp = copyMatrix();
            shoot(i);
            fall();
            play(depth+1);
            recoverMatrix(temp);
        }
    }
 
    static void shoot(int col) {
        int row = -1;
        for (int i = 0; i < h; i++) {
            if (matrix[i][col] == 0) continue;
            row = i;
            break;
        }
        if (row == -1) return;
        List<int[]> stack = new ArrayList<>();
        stack.add(new int[]{row, col});
        while (!stack.isEmpty()) {
            int[] curr = stack.remove(stack.size()-1);
            int x = curr[0], y = curr[1];
            int size = matrix[x][y] - 1;
            matrix[x][y] = 0;
 
            for (int i = 1; i <= size; i++) {
                for (int j = 0; j < 4; j++) {
                    int nx = x + i * dx[j], ny = y + i * dy[j];
                    if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
                    if (matrix[nx][ny] == 0) continue;
                    if (matrix[nx][ny] == 1) {
                        matrix[nx][ny] = 0;
                        continue;
                    }
                    stack.add(new int[]{nx, ny});
                }
            }
        }
    }
 
    static void fall() {
        for (int i = 0; i < w; i++) {
            int bot = h - 1, top = h - 1;
            while(top >= 0) {
                if (matrix[bot][i] == 0) {
                    if (matrix[top][i] != 0) {
                        matrix[bot][i] = matrix[top][i];
                        matrix[top][i] = 0;
                        bot--;
                    }
                    top--;
                } else {
                    top--;
                    bot--;
                }
            }
        }
    }
 
    static int countMatrix() {
        int cnt = 0;
        for (int j = 0; j < w; j++) {
            for (int i = h - 1; i >= 0; i--) {
                if (matrix[i][j] == 0) break;
                cnt++;
            }
        }
        return cnt;
    }
 
    static byte[][] copyMatrix() {
        byte[][] temp = new byte[h][w];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                temp[i][j] = matrix[i][j];
            }
        }
        return temp;
    }
 
    static void recoverMatrix(byte[][] temp) {
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                matrix[i][j] = temp[i][j];
            }
        }
    }
}
