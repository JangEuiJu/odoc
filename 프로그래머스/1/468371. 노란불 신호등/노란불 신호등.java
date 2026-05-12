import java.util.*;

class Solution {
    public int solution(int[][] signals) {
        int answer = 0;
        
        int len = 1;
        for (int i = 0; i < signals.length; i++){
            int g = signals[i][0];
            int y = signals[i][1];
            int r = signals[i][2];
            
            len *= (g+y+r);
        }
        
        int[] arr = new int[len + 1];
        for (int i = 0; i < signals.length; i++){
            int g = signals[i][0];
            int y = signals[i][1];
            int r = signals[i][2];
            
            int offset = (g + y + r);
            
            for(int j = 1; j <= len; j += offset){
                for (int k = 0; k < y; k++){
                    arr[g+j+k]++;
                }
            }      
        }
        for (int i=1; i<=len; i++) {
            if (arr[i] == signals.length) {
                return i;
            }
        }
        
        return -1;
    }
}