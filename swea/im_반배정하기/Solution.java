package im_반배정하기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws Exception {
		StringBuilder sb = new StringBuilder();
		int tc = Integer.parseInt(br.readLine());
		for (int t = 1; t <= tc; t++) {
			sb.append("#" + t);
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int kmin = Integer.parseInt(st.nextToken());
			int kmax = Integer.parseInt(st.nextToken());
			
			int[] scores = new int[n];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++) scores[i] = Integer.parseInt(st.nextToken());
			Arrays.sort(scores);
			
			int ans = Integer.MAX_VALUE;
			for (int i = kmin; i <= kmax; i++) {
				for (int j = i+kmin; j <= i+kmax && j < n-kmin+1; j++) {
					int[] group = {0, 0, 0};
					for (int k = 0; k < n; k++) {
						if (scores[k] < scores[i]) group[0]++;
						else if (scores[k] >= scores[j]) group[2]++;
						else group[1]++;
					}
					
					int min = Integer.MAX_VALUE;
					int max = 0;
					for (int k = 0; k < 3; k++) {
						min = Math.min(min, group[k]);
						max = Math.max(max, group[k]);
					}
					
					if (min < kmin || max > kmax) continue;
					ans = Math.min(ans, max-min);
				}
			}
			
			if (ans == Integer.MAX_VALUE) sb.append(" -1");
			else sb.append(" " + ans);
			sb.append(System.lineSeparator());
		}
		System.out.println(sb.substring(0, sb.length()-1));
	}
}

