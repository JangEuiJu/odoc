import java.math.BigInteger;

class Solution {
    public int solution(int balls, int share) {
        BigInteger top = BigInteger.ONE;
        BigInteger bot = BigInteger.ONE;

        for (int i = balls; i >= balls - share + 1; i--) {
            top = top.multiply(BigInteger.valueOf(i));
        }
        
        for (int i = 1; i <= share; i++) {
            bot = bot.multiply(BigInteger.valueOf(i));
        }

        BigInteger result = top.divide(bot);
        return result.intValue();
    }
}
