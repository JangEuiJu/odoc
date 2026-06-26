import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (list.isEmpty())
                list.add(arr[i]);
            else if (list.get(list.size() - 1) < arr[i])
                list.add(arr[i]);
            else {
                list.remove(list.size() - 1);
                i--;
            }
        }
        
        int[] stk = new int[list.size()];
        int index = 0;
        
        for (int i = 0; i < list.size(); i++) 
            stk[index++] = list.get(i);
        
        return stk;
    }
}