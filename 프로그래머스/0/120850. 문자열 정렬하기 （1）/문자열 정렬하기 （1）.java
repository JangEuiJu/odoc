import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        String str = my_string.replaceAll("[^0-9]", "");
        
        int[] answer = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            answer[i] = str.charAt(i) - '0'; 
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}
