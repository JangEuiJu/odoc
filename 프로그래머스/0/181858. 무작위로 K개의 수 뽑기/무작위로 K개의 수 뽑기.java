import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        Arrays.fill(answer, -1);
        
        Set<Integer> set = new LinkedHashSet<>();
        
        for (int num : arr) {
            set.add(num);
            
            if (set.size() == k)
                break;
        }
        
        int index = 0;
        for (int num : set) {
            answer[index++] = num;
        }
        
        return answer;
    }
}
