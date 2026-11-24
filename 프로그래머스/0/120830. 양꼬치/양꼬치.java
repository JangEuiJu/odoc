class Solution {
    public int solution(int n, int k) {
        int service = n / 10;
        int lambPrice = n * 12000;
        int drinkPrice = Math.max(0, k - service) * 2000;
        return lambPrice + drinkPrice;
    }
}
