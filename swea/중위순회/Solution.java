package 중위순회;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        for (int t = 1; t <= 10; t++) {
            sb.append("#" + t + " ");
            int n = Integer.parseInt(br.readLine());
            
            Node[] nodes = new Node[n+1];
            for (int i = 1; i <= n; i++) {
                nodes[i] = new Node();
            }
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                Node node = nodes[Integer.parseInt(st.nextToken())];
                node.data = st.nextToken();
                if (st.hasMoreTokens()) node.left = nodes[Integer.parseInt(st.nextToken())];
                if (st.hasMoreTokens()) node.right = nodes[Integer.parseInt(st.nextToken())];
            }

            inorderTraversal(nodes[1], sb);
            sb.append(System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static void inorderTraversal(Node node, StringBuilder sb) {
        if (node.left != null) inorderTraversal(node.left, sb);
        sb.append(node.data);
        if (node.right != null) inorderTraversal(node.right, sb);
    }
}

class Node {
    public String data;
    public Node left;
    public Node right;
}
