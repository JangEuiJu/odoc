class Solution {
    public String solution(String my_string, int s, int e) {
        String front = my_string.substring(0, s);
        String target = my_string.substring(s, e + 1);
        String back = my_string.substring(e + 1);
        
        String reversedTarget = new StringBuilder(target).reverse().toString();
        
        return front + reversedTarget + back;
    }
}