import java.util.*;

class Solution {
    public int solution(int[] array, int n) {
        int answer = array[0];
        int minGap = Math.abs(array[0] - n);

        for (int i = 1; i < array.length; i++) {
            int gap = Math.abs(array[i] - n);

            if (gap < minGap) {
                minGap = gap;
                answer = array[i];
            } 
            else if (gap == minGap && array[i] < answer) {
                answer = array[i];
            }
        }

        return answer;
    }
}
