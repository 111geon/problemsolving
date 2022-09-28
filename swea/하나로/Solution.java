package 하나로;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static List<Edge> edges;
    private static long[] x, y;
    private static int[] group, rank;
    private static int n;
    private static double e, ans;

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            n = Integer.parseInt(br.readLine());
            x = new long[n];
            y = new long[n];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) x[i] = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) y[i] = Integer.parseInt(st.nextToken());
            e = Double.parseDouble(br.readLine());

            edges = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                for (int j = i+1; j < n; j++) {
                    edges.add(
                        new Edge(
                            Math.sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j])),
                            i,
                            j
                        )
                    );
                }
            }
            
            edges.sort(Comparator.comparingDouble(o -> o.length));

            rank = new int[n];
            group = new int[n];
            for (int i = 0; i < n; i++) {
                group[i] = i;
            }
            
            ans = 0;
            int v = 0;
            for (Edge edge: edges) {
                if (find(edge.a) == find(edge.b)) continue;
                union(edge.a, edge.b);
                v++;
                ans += e * edge.length * edge.length;
                if (v == n - 1) break;
            }

            sb.append("#" + t + " " + (long)Math.round(ans) + System.lineSeparator());
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

class Edge {
    double length;
    int a;
    int b;

    public Edge(double length, int a, int b) {
        this.length = length;
        this.a = a;
        this.b = b;
    }

    @Override
    public String toString() {
        return length + " " + a + " " + b;
    }
}
