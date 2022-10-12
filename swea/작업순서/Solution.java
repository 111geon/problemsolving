package 작업순서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static int v, e;
  private static List<Integer>[] graph;
  private static boolean[] visited;
  private static Deque<Integer> stack;

  public static void main(String[] args) throws NumberFormatException, IOException {
    StringBuilder sb = new StringBuilder();
    for (int t = 1; t <= 1; t++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      v = Integer.parseInt(st.nextToken());
      e = Integer.parseInt(st.nextToken());
      visited = new boolean[v+1];
      graph = new ArrayList[v+1];
      for (int i = 0; i < v+1; i++) {
        graph[i] = new ArrayList<>();
      }

      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < e; i++) {
        int from = Integer.parseInt(st.nextToken());
        int to = Integer.parseInt(st.nextToken());
        graph[from].add(to);
      }

      stack = new ArrayDeque<>();
      for (int i = 1; i <= v; i++) {
        dfs(i);     
      }

      sb.append("#" + t);
      while (!stack.isEmpty()) {
        sb.append(" " + stack.pollLast());
      }
      sb.append(System.lineSeparator());
    }
    System.out.println(sb.toString());
  }
  
  private static void dfs(int node) {
    if (visited[node]) return;
    visited[node] = true;
    while (!graph[node].isEmpty()) {
      dfs(graph[node].remove(graph[node].size()-1));
    }
    stack.addLast(node);
  }
}
