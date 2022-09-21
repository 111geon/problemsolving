

import java.util.Scanner;

public class View {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {

        for (int i=1; i<=10; i++) {
            System.out.println("#" + i + " " + solution());
        }

    }

    private static int solution() {

        int n = sc.nextInt();
        int[] buildings = new int[n];

        for (int i=0; i<n; i++) {
            buildings[i] = sc.nextInt();
        }

        int[] dxs = {-2, -1, 1, 2};
        int ans = 0;
        for (int i=2; i<n-2; i++) {
            int max_neighbor = 0;
            for(int dx: dxs) {
                max_neighbor = Math.max(max_neighbor, buildings[i+dx]);
            }
            ans += Math.max(0, buildings[i] - max_neighbor);
        }

        return ans;

    }
    
}
