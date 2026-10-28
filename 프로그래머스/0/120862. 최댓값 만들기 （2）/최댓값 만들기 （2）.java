import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        
        int n = numbers.length;
        int case1 = numbers[0] * numbers[1];
        int case2 = numbers[n - 1] * numbers[n - 2];
        
        return Math.max(case1, case2);
    }
}
