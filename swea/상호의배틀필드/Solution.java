package 상호의배틀필드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] dx = {0, -1, 1, 0};
    static int[] dy = {-1, 0, 0, 1};
    static char[] tank = {'<', '^', 'v', '>'};
    static int x, y, d;
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            sb.append("#" + t + " ");

            StringTokenizer st = new StringTokenizer(br.readLine());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            char[][] map = new char[h][w];
            for (int i = 0; i < h; i++) {
                char[] row = br.readLine().toCharArray();
                map[i] = row;
                for (int j = 0; j < w; j++) {
                    switch (row[j]) {
                        case '<':
                        x = i;
                        y = j;
                        d = 0;
                        break;
                        case '^':
                        x = i;
                        y = j;
                        d = 1;
                        break;
                        case 'v':
                        x = i;
                        y = j;
                        d = 2;
                        break;
                        case '>':
                        x = i;
                        y = j;
                        d = 3;
                        break;
                    }
                }
            }

            int n = Integer.parseInt(br.readLine());
            String commands = br.readLine();
            for (int i = 0; i < n; i++) {
                switch(commands.charAt(i)) {
                    case 'U':
                    move(map, h, w, 1);
                    break;
                    case 'D':
                    move(map, h, w, 2);
                    break;
                    case 'L':
                    move(map, h, w, 0);
                    break;
                    case 'R':
                    move(map, h, w, 3);
                    break;
                    case 'S':
                    shoot(map, h, w);
                    break;
                }
            }

            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    sb.append(map[i][j]);
                }
                sb.append(System.lineSeparator());
            }
        }
        System.out.println(sb.toString());
    }

    private static void move(char[][] map, int h, int w, int nd) {
        d = nd;
        map[x][y] = tank[d];

        int nx = x + dx[d];
        int ny = y + dy[d];
        if (nx >= h || nx < 0 || ny >= w || ny < 0) return;
        if (map[nx][ny] == '.') {
            map[x][y] = '.';
            x = nx;
            y = ny;
            map[x][y] = tank[d];
        }
    }

    private static void shoot(char[][] map, int h, int w) {
        int i = 1;
        int nx, ny;
        while (true) {
            nx = x + i * dx[d];
            ny = y + i * dy[d];
            if (nx >= h || nx < 0 || ny >= w || ny < 0) break;
            if (map[nx][ny] == '#') break;
            if (map[nx][ny] == '*') {
                map[nx][ny] = '.';
                break;
            }
            i++;
        }
    }
}
