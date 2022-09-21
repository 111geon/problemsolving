

import java.util.Scanner;

public class Flatten {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        for (int tc=1; tc<=10; tc++) {
            System.out.println("#" + tc + " " + solution());
        }
    }

    private static int solution() {
        int n = sc.nextInt();
        int[] heights = new int[100];
        for (int i=0; i<100; i++) {
            heights[i] = sc.nextInt();
        }

        for (int i=0; i<n; i++) {
            int maxH = 0;
            int minH = Integer.MAX_VALUE;
            for (int height: heights) {
                maxH = Math.max(maxH, height);
                minH = Math.min(minH, height);
            }

            for (int j=0; j<100; j++) {
                if (heights[j] == maxH) {
                    heights[j]--;
                    break;
                }
            }
            for (int j=0; j<100; j++) {
                if (heights[j] == minH) {
                    heights[j]++;
                    break;
                }
            }
        }

        int maxH = 0;
        int minH = Integer.MAX_VALUE;
        for (int height: heights) {
            maxH = Math.max(maxH, height);
            minH = Math.min(minH, height);
        }

        return maxH - minH;
    }
}
