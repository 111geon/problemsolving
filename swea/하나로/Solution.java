package 하나로;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
 
public class Solution {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
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

            ans = 0;
            kruskal();
            // prim();
 
            sb.append("#" + t + " " + (long)Math.round(e * ans) + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static void prim() {
        double[][] edges = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                double edge = (x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]);
                edges[i][j] = edge;
                edges[j][i] = edge;
            }
        }

        boolean[] visited = new boolean[n];
        PriorityQueue<Node> q = new PriorityQueue<>(Comparator.comparingDouble(node -> node.length));
        q.add(new Node(0.0, 0));
        double[] minLength = new double[n];
        Arrays.fill(minLength, Double.MAX_VALUE);
        while (!q.isEmpty()) {
            Node curr = q.poll();
            if (visited[curr.node]) continue;
            visited[curr.node] = true;
            ans += curr.length;
            for (int i = 0; i < n; i++) {
                if (visited[i]) continue;
                Double length = edges[curr.node][i];
                if (length < minLength[i]) {
                    q.add(new Node(length, i));
                    minLength[i] = length;
                }
                
            }
        }
    }

    private static void kruskal() {
        PriorityQueue<Edge> edgesHeap = new PriorityQueue<>(Comparator.comparingDouble(edge -> edge.length));
        
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                edgesHeap.add(
                    new Edge(
                        (x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]),
                        i,
                        j
                    )
                );
            }
        }

        rank = new int[n];
        group = new int[n];
        for (int i = 0; i < n; i++) {
            group[i] = i;
        }
        
        int v = 0;
        while (!edgesHeap.isEmpty()) {
            Edge edge = edgesHeap.poll();
            if (find(edge.a) == find(edge.b)) continue;
            union(edge.a, edge.b);
            v++;
            ans += edge.length;
            if (v == n - 1) break;
        }
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

class Node {
    double length;
    int node;

    public Node(double length, int node) {
        this.length = length;
        this.node = node;
    }
}
