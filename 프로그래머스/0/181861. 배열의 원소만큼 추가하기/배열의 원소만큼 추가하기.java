import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int a : arr) {
            for (int j = 0; j < a; j++) {
                list.add(a);
            }
        }
        return list.stream().mapToInt(i -> i).toArray();
    }
}