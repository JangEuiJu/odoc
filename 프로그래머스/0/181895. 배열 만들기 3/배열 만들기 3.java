import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        List<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < 2; i++) {
            for (int j = intervals[i][0]; j <= intervals[i][1]; j++) {
                list.add(arr[j]);
            }
        }
        
        return list.stream().mapToInt(i -> i).toArray();
    }
}