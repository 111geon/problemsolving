package swea.SSAFY;

import java.util.Scanner;

public class 회문2 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        for (int t = 1; t <= 10; t++) {
            sc.nextLine();
            int ans = 1;
            StringBuffer[] cols = new StringBuffer[100];
            for (int i=0; i<100; i++) {
                cols[i] = new StringBuffer();
            }

            for (int i = 0; i < 100; i++) {
                String row = sc.nextLine().trim();

                ans = Math.max(ans, maxPalindrome(row, ans));

                for (int j = 0; j < 100; j++) {
                    cols[j].append(row.substring(j, j+1));
                }
            }

            for (int i=0; i<100; i++) {
                String col = cols[i].toString();
                ans = Math.max(ans, maxPalindrome(col, ans));
            }

            System.out.println("#" + t + " " + ans);

        }
    }

    private static int maxPalindrome(String string, int max) {
        for (int n = string.length(); n > max; n--) {
            if (hasNPalindrome(string, n)) {
                return n;
            }
        }

        return max;
    }

    private static boolean hasNPalindrome(String string, int n) {
        for (int i = 0; i < string.length() - n + 1; i++) {
            if (isPalindrome(string.substring(i, i+n))) {
                return true;
            }
        }
        return false;
    }

    private static boolean isPalindrome(String string) {
        int start = 0, end = string.length() - 1;
        while (start < end) {
            if (string.charAt(start) != string.charAt(end)) { return false; }
            start++;
            end--;
        }
        return true;
    }
}
