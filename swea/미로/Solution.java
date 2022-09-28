package 미로;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static Byte[][] maze = new Byte[16][16];
    private static Byte[] start;
    private static final Byte[] dx = new Byte[]{0, 1, 0, -1};
    private static final Byte[] dy = new Byte[]{1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        for (int t = 1; t <= 1; t++) {
            br.readLine();
            for (byte i = 0; i < 16; i++) {
                String[] row = br.readLine().split("");
                for (byte j = 0; j < 16; j++) {
                    maze[i][j] = Byte.parseByte(row[j]);
                    if (maze[i][j] == 2) {
                        start = new Byte[]{i, j};
                    }
                }
            }

            sb.append("#" + t + " " + dfs(start) + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static byte dfs(Byte[] start) {
        boolean[][] visited = new boolean[16][16];
        List<Byte[]> stack = new ArrayList<>();
        stack.add(start);

        while (!stack.isEmpty()) {
            Byte[] curr = stack.get(stack.size()-1);
            byte x = curr[0], y = curr[1];

            if (maze[x][y] == 3) return 1;

            boolean hasMore = false;
            for (byte i = 0; i < 4; i++) {
                byte nx = (byte) (x + dx[i]), ny = (byte) (y + dy[i]);
                if (!visited[nx][ny] && maze[nx][ny] != 1) {
                    hasMore = true;
                    visited[nx][ny] = true;
                    stack.add(new Byte[]{nx, ny});
                    break;
                }
            }
            if (!hasMore) stack.remove(stack.size()-1);
        }

        return 0;
    }
}