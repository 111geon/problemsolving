package 점심식사시간;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;
  
public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static List<Person> people;
    static List<Stair> stairs;
  
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            n = Integer.parseInt(br.readLine());
            people = new ArrayList<>();
            stairs = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    int element = Integer.parseInt(st.nextToken());
                    if (element == 0) continue;
                    if (element == 1) {
                        people.add(new Person(i, j));
                    } else {
                        stairs.add(new Stair(i, j, element));
                    }
                }
            }

            for (Person person: people) {
                for (int i = 0; i < 2; i++) {
                    person.distToStair[i] = Math.abs(person.x - stairs.get(i).x) + Math.abs(person.y - stairs.get(i).y);
                }
            }

            int ans = Integer.MAX_VALUE;
            for (int i = 0; i < 1 << people.size(); i++) {
                for (int j = 0; j < people.size(); j++) {
                    int stairNum = (i & 1 << j) > 0 ? 1 : 0;
                    stairs.get(stairNum).q.add(people.get(j).distToStair[stairNum]);
                }
                ans = Math.min(ans, Math.max(stairs.get(0).getTime(), stairs.get(1).getTime()));
                stairs.get(0).q.clear();
                stairs.get(1).q.clear();
            }
            sb.append("#" + t + " " + (ans + 1) + System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}

class Person {
    int x;
    int y;
    int[] distToStair;

    public Person(int x, int y) {
        this.x = x;
        this.y = y;
        this.distToStair = new int[2];
    }

    @Override
    public String toString() {
        return "Person [distToStair=" + Arrays.toString(distToStair) + ", x=" + x + ", y=" + y + "]";
    }
}

class Stair {
    int x;
    int y;
    int depth;
    List<Integer> q;

    public Stair(int x, int y, int depth) {
        this.x = x;
        this.y = y;
        this.depth = depth;
        this.q = new ArrayList<>();
    }

    public int getTime() {
        Collections.sort(q);
        if (q.isEmpty()) return 0;
        if (q.size() > 3) {
            for (int i = 3; i < q.size(); i++) {
                q.set(i, Math.max(q.get(i), q.get(i-3) + depth));
            }
        }
        return q.get(q.size()-1) + depth;
    }

    @Override
    public String toString() {
        return "Stair [depth=" + depth + ", q=" + q + ", x=" + x + ", y=" + y + "]";
    }
}
