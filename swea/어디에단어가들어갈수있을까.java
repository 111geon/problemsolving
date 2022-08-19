package swea.SSAFY;

import java.util.Scanner;

public class 어디에단어가들어갈수있을까 {
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) throws Exception {
        int tc = sc.nextInt();
        int n, k;
        for (int t = 1; t <= tc; t++) {
            int ans = 0;
            n = sc.nextInt();
            k = sc.nextInt();
            sc.nextLine();

            StringBuffer patTemp = new StringBuffer();
            patTemp.append("0");
            for (int i = 0; i < k; i++) {
                patTemp.append("1");
            }
            patTemp.append("0");
            String pat = patTemp.toString();

            char[][] cols = new char[n][n+2];
            for (int i = 0; i < n; i++) {
                cols[i][0] = '0';
                cols[i][n+1] = '0';
            }

            for (int i = 0; i < n; i++) {
                String row = String.join("", sc.nextLine().split(" "));
                
                for (int j = 0; j < row.length(); j++) {
                    cols[j][i+1] = row.charAt(j);
                }

                row = "0" + row + "0";
                ans += containsAll(row, pat);

            }

            for (int i = 0; i < n; i++) {
                ans += containsAll(new String(cols[i]), pat);
            }

            System.out.println("#" + t + " " + ans);

        }
    }

    private static int containsAll(String ground, String pat) {
        int patIdx = ground.indexOf(pat);

        if (patIdx == -1) {
            return 0;
        }        

        return 1 + containsAll(ground.substring(patIdx+1), pat);
    }
}
