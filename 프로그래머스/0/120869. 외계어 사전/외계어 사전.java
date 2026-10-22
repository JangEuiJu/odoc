import java.util.Arrays;

class Solution {
    public int solution(String[] spell, String[] dic) {
        Arrays.sort(spell);
        String target = String.join("", spell);

        for (String d : dic) {
            char[] arr = d.toCharArray();
            Arrays.sort(arr);
            String sortedWord = new String(arr);

            if (sortedWord.equals(target)) {
                return 1; 
            }
        }
        
        return 2;
    }
}
