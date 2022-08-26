package ps.오목판정;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            sb.append("#" + t);
            int n = Integer.parseInt(br.readLine());
            char[][] omok = new char[n][n];
            for (int i = 0; i < n; i++) {
                omok[i] = br.readLine().trim().toCharArray();
            }

            sb.append(" " + yesOrNo(n, omok) + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static String yesOrNo(int n, char[][] omok) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (omok[i][j] == 'o' && check(n, omok, i, j)) return "YES";
            }
        }
        return "NO";
    }

    private static boolean check(int n, char[][] omok, int x, int y) {
        int[] dx = {1, 1, 1, 0};
        int[] dy = {-1, 0, 1, 1};
        
        for (int i = 0; i < dx.length; i++) {
            for (int j = 1; j <= 5; j++) {
                if (j == 5) return true;

                int nx = x + j * dx[i];
                int ny = y + j * dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) break;
                if (omok[nx][ny] == '.') break;
            }
        }
        return false;
    }
}
