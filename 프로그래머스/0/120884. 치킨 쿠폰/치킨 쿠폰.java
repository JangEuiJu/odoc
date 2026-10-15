class Solution {
    public int solution(int chicken) {
        int serviceChicken = 0;
        int coupon = chicken; 

        while (coupon >= 10) {
            int newService = coupon / 10;
            serviceChicken += newService;

            coupon = (coupon % 10) + newService;
        }

        return serviceChicken;
    }
}
