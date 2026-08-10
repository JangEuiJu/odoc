class Solution {
    public int solution(String myString, String pat) {
        String changed = myString.replace("A", "C")
                                 .replace("B", "A")
                                 .replace("C", "B");
                                 
        return changed.contains(pat) ? 1 : 0;
    }
}