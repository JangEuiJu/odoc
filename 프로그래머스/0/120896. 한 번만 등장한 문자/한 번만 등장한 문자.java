import java.util.Arrays;

class Solution {
    public String solution(String s) {
        int[] count = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < count.length; i++) {
            if (count[i] == 1) {
                sb.append((char) ('a' + i));
            }
        }
        
        return sb.toString();
    }
}
