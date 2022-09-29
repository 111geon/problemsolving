package 창용마을무리의개수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;
 
public class Solution {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int[] group, rank;
    private static int n, m;
 
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            rank = new int[n+1];
            group = new int[n+1];
            for (int i = 1; i <= n; i++) {
                group[i] = i;
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
                union(a, b);
            }

            Set<Integer> groups = new HashSet<>();
            for (int i = 1; i <= n; i++) {
                groups.add(find(i));
            }
 
            sb.append("#" + t + " " + groups.size() + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
 
    private static int find(int node) {
        if (group[node] == node) return node;
        group[node] = find(group[node]);
        return group[node];
    }
 
    private static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return;
        if (rank[a] > rank[b]) {
            group[b] = a;
        } else if (rank[a] < rank[b]) {
            group[a] = b;
        } else {
            group[b] = a;
            rank[a]++;
        }
    }
}
