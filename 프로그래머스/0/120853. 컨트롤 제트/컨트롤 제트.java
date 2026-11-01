import java.util.Stack;

class Solution {
    public int solution(String s) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();

        for (String str : s.split(" ")) {
            if (str.equals("Z")) {
                if (!stack.isEmpty()) {
                    stack.pop(); 
                }
            } else {
                stack.push(Integer.parseInt(str)); 
            }
        }

        for (int num : stack) {
            answer += num;
        }

        return answer;
    }
}
