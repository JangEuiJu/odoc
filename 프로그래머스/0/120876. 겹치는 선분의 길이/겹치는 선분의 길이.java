import java.util.Arrays;

class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        int[] count = new int[201]; 

        for (int[] line : lines) {
            int left = line[0] + 100;
            int right = line[1] + 100;

            for (int i = left; i < right; i++) {
                count[i]++;
            }
        }

        for (int i = 0; i < count.length; i++) {
            if (count[i] >= 2) {
                answer++;
            }
        }

        return answer;
    }
}
