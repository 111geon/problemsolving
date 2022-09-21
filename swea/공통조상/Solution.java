package 공통조상;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            StringBuilder sb = new StringBuilder();
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int[][] tree = new int[v+1][3];  // [노드번호][부모, 왼쪽자식, 오른쪽자식]
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < e; i++) {
                int p = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                tree[c][0] = p;
                if (tree[p][1] == 0) tree[p][1] = c;
                else tree[p][2] = c;
            }

            int levelA = 0, levelB = 0;
            int temp = a;
            while (temp != 1) {
                temp = tree[temp][0];
                levelA++;
            }
            temp = b;
            while (temp != 1) {
                temp = tree[temp][0];
                levelB++;
            }

            while (levelA != levelB) {
                if (levelA > levelB) {
                    a = tree[a][0];
                    levelA--;
                } else {
                    b = tree[b][0];
                    levelB--;
                }
            }

            while (a != b) {
                a = tree[a][0];
                b = tree[b][0];
            }
            
            sb.append("#" + t + " " + a + " " + size(tree, a));
            System.out.println(sb.toString());
        }
    }

    private static int size(int[][] tree, int node) {
        if (node == 0) return 0;
        return 1 + size(tree, tree[node][1]) + size(tree, tree[node][2]);
    }
}
