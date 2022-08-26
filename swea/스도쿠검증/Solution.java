package ps.스도쿠검증;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            int[][] sudoku = new int[9][9];
            for (int i = 0; i < 9; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 9; j++) {
                    sudoku[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            sb.append("#" + t + " " + check(sudoku) + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static int check(int[][] sudoku) {
        Set<Integer> visited = new HashSet<>();
        for (int i = 0; i < 9; i++) {
            visited = new HashSet<>();
            for (int j = 0; j < 9; j++) visited.add(sudoku[i][j]);
            if (visited.size() != 9) return 0;
        }

        for (int i = 0; i < 9; i++) {
            visited = new HashSet<>();
            for (int j = 0; j < 9; j++) visited.add(sudoku[j][i]);
            if (visited.size() != 9) return 0;
        }

        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                visited = new HashSet<>();
                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        visited.add(sudoku[i+k][j+l]);
                    }
                }
                if (visited.size() != 9) return 0;
            }
        }

        return 1;
    }
}
