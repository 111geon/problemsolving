package Contact;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;
  
public class Solution {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n, start;
    private static Set<Integer>[] graph;
  
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        for (int t = 1; t <= 10; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            start = Integer.parseInt(st.nextToken());
            graph = new Set[101];
            Arrays.setAll(graph, element -> new HashSet<>());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n / 2; i++) {
                graph[Integer.parseInt(st.nextToken())].add(Integer.parseInt(st.nextToken()));
            } 
             
            List<Integer> firstQ = new ArrayList<>();
            List<Integer> secondQ = new ArrayList<>();
            boolean[] visited = new boolean[101];
            visited[start] = true;
            firstQ.add(start);
            while (true) {
                for (int node: firstQ) {
                    for (int nexthop: graph[node]) {
                        if (visited[nexthop]) continue;
                        visited[nexthop] = true;
                        secondQ.add(nexthop);
                    }
                }
                if (secondQ.isEmpty()) break;
                firstQ = new ArrayList<>(secondQ);
                secondQ = new ArrayList<>();
            }
 
            int ans = 0;
            for (int node: firstQ) {
                ans = Math.max(ans, node);
            }
  
            sb.append("#" + t + " " + ans + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}