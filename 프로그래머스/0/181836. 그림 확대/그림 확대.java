import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] solution(String[] picture, int k) {
        List<String> result = new ArrayList<>();
        
        for (String row : picture) {
            StringBuilder sb = new StringBuilder();
            
            for (int j = 0; j < row.length(); j++) {
                sb.append(String.valueOf(row.charAt(j)).repeat(k));
            }
            
            String expandedRow = sb.toString();
            for (int i = 0; i < k; i++) {
                result.add(expandedRow);
            }
        }
        
        return result.toArray(new String[0]);
    }
}
