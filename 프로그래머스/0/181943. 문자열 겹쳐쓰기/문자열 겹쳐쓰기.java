class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        int l1 = overwrite_string.length();
        int l2 = my_string.length();
        
        answer = my_string.substring(0, s) + overwrite_string + my_string.substring(s+l1, l2);
        
        return answer;
    }
}