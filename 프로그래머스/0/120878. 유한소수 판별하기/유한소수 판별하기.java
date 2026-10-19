public class Solution {
    public int solution(int a, int b) {
        int gcd = getGcd(a, b);
        b = b / gcd; 

        while (b % 2 == 0) {
            b /= 2;
        }
        while (b % 5 == 0) {
            b /= 5;
        }

        return (b == 1) ? 1 : 2;
    }

    private int getGcd(int n1, int n2) {
        if (n2 == 0) {
            return n1;
        }
        return getGcd(n2, n1 % n2);
    }
}
