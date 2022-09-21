

import java.util.Scanner;

public class 초심자의회문검사 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        int tc = sc.nextInt();
        sc.nextLine();
        for (int t = 1; t <= tc; t++) {
            String testee = sc.nextLine().strip();
            int ans = 1;
            int n = testee.length();
            for (int i = 0; i < n / 2; i++) {
                if (testee.charAt(i) != testee.charAt(n-i-1)) {
                    ans = 0;
                    break;
                }
            }

            System.out.println("#" + t + " " + ans);
        }
    }
}
