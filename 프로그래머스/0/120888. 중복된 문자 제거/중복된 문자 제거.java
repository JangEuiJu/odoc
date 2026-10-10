import java.util.LinkedHashSet;

public class Solution {
    public String solution(String myString) {
        LinkedHashSet<Character> set = new LinkedHashSet<>();
        for (char c : myString.toCharArray()) {
            set.add(c);
        }

        StringBuilder sb = new StringBuilder();
        for (char c : set) {
            sb.append(c);
        }
        return sb.toString();
    }
}
