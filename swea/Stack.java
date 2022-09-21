

import java.util.ArrayList;
import java.util.List;

public class Stack {
    public static void main(String[] args) throws Exception {
        YGStack<Integer> stack = new YGStack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());

        String test1 = "()()((()))";
        String test2 = "(()))";

        System.out.println(test(test1));
        System.out.println(test(test2));
    }

    private static boolean test(String t) {
        List<Character> list = new ArrayList<>();

        for (int i = 0; i < t.length(); i++) {
            char curr = t.charAt(i);
            if (!list.isEmpty() && list.get(list.size()-1) == '(' && curr == ')') {
                list.remove(list.size()-1);
            }
            else {
                list.add(curr);
            }   
        }

        if (list.isEmpty()) { return true; }
        return false;
    }
}

class YGStack<T extends Number> {
    List<T> list = new ArrayList<>();

    public void push(T item) {
        list.add(item);
    }

    public T pop() {
        T popped = list.get(list.size()-1);
        list.remove(list.size()-1);
        return popped;
    }
}
