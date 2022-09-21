package 요세푸스;


import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 요세푸스 {
  private static Scanner sc = new Scanner(System.in);
  public static void main(String[] args) {
    int n = sc.nextInt();
    int k = sc.nextInt();

    Node node = createLinkedCircle(n);
    List<Integer> ans = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < k - 1; j++) node = node.next;
      ans.add(node.data);
      node.prev.next = node.next;
      node.next.prev = node.prev;
      node = node.next;
    }

    String ansStr = ans.toString();
    System.out.print("<");
    System.out.print(ansStr.substring(1, ansStr.length()-1));
    System.out.print(">");

  }

  public static Node createLinkedCircle(int n) {
    Node root = new Node(1);
    if (n==1) {
      root.next = root;
      root.prev = root;
      return root;
    }

    Node node = root;
    for (int i = 2; i < n; i++) {
      Node nextNode = new Node(i);
      node.next = nextNode;
      nextNode.prev = node;
      node = node.next;
    }

    Node end = new Node(n);
    node.next = end;
    end.prev = node;
    end.next = root;
    root.prev = end;

    return root;
  }
}

class Node {
  public int data;
  public Node prev;
  public Node next;

  public Node(int data) {
    this.data = data;
  }
}
