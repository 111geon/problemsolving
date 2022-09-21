package 암호문3;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 암호문3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int t = 1; t <= 10; t++) {
            StringBuilder sb = new StringBuilder();
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            Node node = new Node(Integer.parseInt(st.nextToken()));
            Node head = node;
            for (int i = 0; i < n-1; i++) {
                node.link = new Node(Integer.parseInt(st.nextToken()));
                node = node.link;
            }
            Node tail = node;

            int m = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            String command;
            Node tempNode;
            int x, y;
            for (int i = 0; i < m; i++) {
                node = head;
                command = st.nextToken();

                if (command.equals("I")) {
                    x = Integer.parseInt(st.nextToken());
                    y = Integer.parseInt(st.nextToken());

                    if (x==0) {
                        tempNode = head;
                        head = new Node(Integer.parseInt(st.nextToken()));
                        node = head;
                    } else {
                        for (int j = 0; j < x-1; j++) node = node.link;
                        tempNode = node.link;
                        node.link = new Node(Integer.parseInt(st.nextToken()));
                        node = node.link;
                    }

                    for (int j = 0; j < y-1; j++) {
                        node.link = new Node(Integer.parseInt(st.nextToken()));
                        node = node.link;
                    }
                    node.link = tempNode;
                    if (tempNode == null) tail = node;
                }

                if (command.equals("D")) {
                    x = Integer.parseInt(st.nextToken());
                    y = Integer.parseInt(st.nextToken());

                    for (int j = 0; j < x-1; j++) node = node.link;
                    tempNode = node;
                    for (int j = 0; j < y; j++) node = node.link;
                    if (x==0) {
                        head = node;
                    } else {
                        tempNode.link = node.link;
                        if (tempNode.link == null) tail = tempNode;
                    }
                }

                if (command.equals("A")) {
                    y = Integer.parseInt(st.nextToken());

                    node = tail;
                    for (int j = 0; j < y; j++) {
                        node.link = new Node(Integer.parseInt(st.nextToken()));
                        node = node.link;
                    }
                    tail = node;
                }
            }

            for (int i = 0; i< 10; i++) {
                sb.append(" " + head.data);
                head = head.link;
            }

            System.out.println("#" + t + sb.toString());
        }
    }
}

class Node {
    public int data;
    public Node link;

    public Node(int data) {
        this.data = data;
    }
}
