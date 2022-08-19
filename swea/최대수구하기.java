package swea.SSAFY;

import java.util.Arrays;
import java.util.Scanner;

public class 최대수구하기 {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        int ntc = Integer.parseInt(sc.nextLine().trim());
        for (int tc=1; tc<=ntc; tc++) {
            System.out.println("#" + tc + " " + 
            Arrays.stream(sc.nextLine().split(" "))
                .map(Integer::parseInt)
                .max(Integer::compare)
                .get()
            );
            
        }
    }
}
