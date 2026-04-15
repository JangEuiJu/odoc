import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int len = sc.nextInt();
        String train = sc.next();
        
        int answer = 0;
        for (int i = 0; i < len - 1; i++) {
            String now = train.substring(i, i + 2);
            answer += getRoomCnt(now);
        }
        System.out.println(answer);
        sc.close();
    }

    private static int getRoomCnt(String now) {
        if (now.equals("][")) return 0;
        if (now.equals("55") || now.equals("22")) return 2;
        return 1;
    }
}