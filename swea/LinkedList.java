public class LinkedList {
    public Node root;
    public Node end;

    public LinkedList(Node root) {
        this.root = root;
        this.end = root;
    }

    public static void main(String[] args) {
        LinkedList ll = new LinkedList(new Node(5));
        ll.append(new Node(6));
        ll.appendLeft(new Node(4));

        ll.print();


    }

    public void print() {
        Node node = root;
        while (node != null) {
            if (node == root) {
                System.out.print("root: ");
            }
            if (node == end) {
                System.out.println("end: " + node.data);
                return;
            }
            System.out.print(node.data + " -> ");
            node = node.next;
        }
    }

    public void append(Node node) {
        node.prev = end;
        end.next = node;
        end = node;
    }

    public void appendLeft(Node node) {
        node.next = root;
        root.prev = node;
        root = node;
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
