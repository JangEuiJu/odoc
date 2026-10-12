class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String kStr = String.valueOf(k); 

        for (int num = i; num <= j; num++) {
            String str = String.valueOf(num); 
            
            for (int c = 0; c < str.length(); c++) {
                if (String.valueOf(str.charAt(c)).equals(kStr)) {
                    answer++;
                }
            }
        }
        return answer;
    }
}
