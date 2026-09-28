class Solution {
    public int solution(String my_string) {
        String[] parts = my_string.split(" ");
        int answer = Integer.parseInt(parts[0]);
        
        for (int i = 1; i < parts.length; i += 2) { 
            String op = parts[i];
            int num = Integer.parseInt(parts[i + 1]);
            
            if (op.equals("+")) {
                answer += num;
            } else if (op.equals("-")) {
                answer -= num;
            }
        }
        
        return answer;
    }
}
