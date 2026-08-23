import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        List<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < rank.length; i++) {
            if (attendance[i]) {
                list.add(rank[i]);
            }
        }
        
        Collections.sort(list);
        
        int aIdx = getIndex(rank, list.get(0));
        int bIdx = getIndex(rank, list.get(1));
        int cIdx = getIndex(rank, list.get(2));
        
        return 10000 * aIdx + 100 * bIdx + cIdx;
    }
    
    private int getIndex(int[] rank, int target) {
        for (int i = 0; i < rank.length; i++) {
            if (rank[i] == target) return i;
        }
        return -1;
    }
}
