package 정렬;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
  private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws NumberFormatException, IOException {
    int tc = Integer.parseInt(br.readLine());
    StringBuilder sb = new StringBuilder();
    for (int t = 1; t <= tc; t++) {
      int n = Integer.parseInt(br.readLine());
      StringTokenizer st = new StringTokenizer(br.readLine());
      int[] ls = new int[n];
      for (int i = 0; i < n; i++) {
        ls[i] = Integer.parseInt(st.nextToken());
      }

      // mergeSort(ls, 0, n);
      quickSort(ls, 0, n-1);
      
      sb.append("#" + t);
      for (int i = 0; i < n; i++) {
        sb.append(" " + ls[i]);
      }
      sb.append(System.lineSeparator());
    }
    System.out.println(sb.toString());
  }

  private static void quickSort(int[] ls, int start, int end) {
    if (start >= end) return;

    int l = start, r = end - 1, pivot = end;

    // 최악의 경우를 피하기 위해 mid와 pivot을 교환
    int mid = (start + pivot) / 2;
    int temp = ls[mid];
    ls[mid] = ls[pivot];
    ls[pivot] = temp;

    while (l <= r) {
      while (l < pivot && ls[l] <= ls[pivot]) {
        l++;
      }
      while (start <= r && ls[r] >= ls[pivot]) {
        r--;
      }
      if (l < r) {
        temp = ls[r];
        ls[r] = ls[l];
        ls[l] = temp;
      } else {
        temp = ls[pivot];
        ls[pivot] = ls[l];
        ls[l] = temp;
      }
    }

    quickSort(ls, start, r);
    quickSort(ls, l + 1, end);
  }

  private static void mergeSort(int[] ls, int start, int end) {
    if (end - start <= 1) return;
    int mid = (start + end) / 2;
    mergeSort(ls, start, mid);
    mergeSort(ls, mid, end);

    int[] l = Arrays.copyOfRange(ls, start, mid);
    int[] r = Arrays.copyOfRange(ls, mid, end);
    int i = start, il = 0, ir = 0;
    
    while (il < l.length && ir < r.length) {
      if (l[il] < r[ir]) {
        ls[i++] = l[il++];
      } else {
        ls[i++] = r[ir++];
      }
    }

    while (il < l.length) {
      ls[i++] = l[il++];
    }
    while (ir < r.length) {
      ls[i++] = r[ir++];
    }
  }
}
