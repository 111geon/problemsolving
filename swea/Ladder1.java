

import java.util.Scanner;

public class Ladder1 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        for (int t = 1; t <= 10; t++) {
            int ans = 0;
            sc.nextInt();
            int[][] graph = new int[100][100];
            for (int i = 0; i < 100; i++) {
                for (int j = 0; j < 100; j++) {
                    graph[i][j] = sc.nextInt();
                }
            }

            while (true) {
                int start = 0;
                int x = 0;
                int y = 0;
                for (int i = 0; i < 100; i++) {
                    if (graph[0][i] == 1) {
                        start = y = i;
                        graph[0][y] = 0;
                        break;
                    }
                }

                while (x < 100) {
                    if (y-1 >= 0 && graph[x][y-1] == 1) {
                        while (y-1 >= 0 && graph[x][y-1] == 1) {
                            y--;
                        }
                    } else if (y+1 < 100 && graph[x][y+1] == 1) {
                        while (y+1 < 100 && graph[x][y+1] == 1) {
                            y++;
                        }
                    }
                    x++;
                }
                x--;
                
                if (graph[x][y] == 2) { 
                    ans = start;
                    break; 
                }
            }

            System.out.println("#" + t + " " + ans);
        }
    }
}
