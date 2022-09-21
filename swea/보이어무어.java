

import java.util.Scanner;

public class 보이어무어 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        for (int t = 1; t <= 10; t++) {
            int ans = 0;

            sc.next();
            String pat = sc.next();
            String com = sc.next();

            int iPat = pat.length() - 1;
            int iCom = iPat;
            while (iCom < com.length()) {
                if (com.charAt(iCom) == pat.charAt(iPat)) {
                    if (com.substring(iCom - pat.length() + 1, iCom + 1).equals(pat)) {
                        ans++;
                    }
                    iCom += pat.length();
                } else {
                    while (iPat >= 0 && pat.charAt(iPat) != com.charAt(iCom)) {
                        iPat--;
                    }
                    iCom += pat.length() - iPat - 1;
                    iPat = pat.length() - 1;
                }
            }

            System.out.println("#" + t + " " + ans);
        }
    }
}
