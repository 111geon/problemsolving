package ps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 힙 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            sb.append("#" + t);
            int n = Integer.parseInt(br.readLine());
            List<Integer> heap = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String command = st.nextToken();
                if (command.equals("1")) {
                    heapPush(heap, Integer.parseInt(st.nextToken()));
                } else if (command.equals("2")) {
                    sb.append(" " + heapPop(heap));
                }
            }
            sb.append(System.lineSeparator());
        }
        sb.delete(sb.length()-1, sb.length());
        System.out.println(sb.toString());
    }

    private static void heapPush(List<Integer> heap, int num) {
        heap.add(num);

        int i = heap.size() - 1;
        int iParent, temp;
        while (i != 0) {
            iParent = (i-1)/2;
            if (heap.get(i) <= heap.get(iParent)) break;
            temp = heap.get(i);
            heap.set(i, heap.get(iParent));
            heap.set(iParent, temp);
            i = iParent;
        }

        System.out.println(heap);
    }

    private static int heapPop(List<Integer> heap) {
        if (heap.size() == 0) return -1;

        int popped = heap.get(0);
        heap.set(0, heap.get(heap.size()-1));
        heap.remove(heap.size()-1);

        int i = 0;
        int temp, iLeftChild, iRightChild, iBigger;
        int halfSize = heap.size() / 2;
        while (i < halfSize) {
            iLeftChild = i * 2 + 1;
            iRightChild = i * 2 + 2;
            if (iRightChild >= heap.size()) {
                if (heap.get(i) >= heap.get(iLeftChild)) break;
                temp = heap.get(i);
                heap.set(i, heap.get(iLeftChild));
                heap.set(iLeftChild, temp);
                i = iLeftChild;
            } else {
                if (heap.get(iLeftChild) > heap.get(iRightChild)) iBigger = iLeftChild;
                else iBigger = iRightChild;
                if (heap.get(i) >= heap.get(iBigger)) break;                
                temp = heap.get(i);
                heap.set(i, heap.get(iBigger));
                heap.set(iBigger, temp);
                i = iBigger;
            }
        }
        System.out.println(heap);
        return popped;
    }
}
