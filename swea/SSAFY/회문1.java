package swea.SSAFY;

import java.util.Scanner;

public class 회문1 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        for (int t = 1; t <= 10; t++) {
            int ans = 0;
            int n = sc.nextInt();
            StringBuffer[] cols = new StringBuffer[8];
            for (int i=0; i<8; i++) {
                cols[i] = new StringBuffer();
            }

            for (int i = 0; i < 8; i++) {
                String row = sc.next();
                ans += numPalindrome(row, n);

                for (int j = 0; j < 8; j++) {
                    cols[j].append(row.substring(j, j+1));
                }
            }

            for (int i=0; i<8; i++) {
                String col = cols[i].toString();
                ans += numPalindrome(col, n);
            }

            System.out.println("#" + t + " " + ans);

        }
    }

    private static int numPalindrome(String string, int n) {
        int ans = 0;
        for (int i = 0; i < string.length() - n + 1; i++) {
            if (isPalindrome(string.substring(i, i+n))) {
                ans++;
            }
        }
        return ans;
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
