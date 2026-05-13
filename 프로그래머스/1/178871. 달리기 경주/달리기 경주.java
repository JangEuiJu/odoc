import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < players.length; i++)
            map.put(players[i], i);
            
        for (int i = 0; i < callings.length; i++){
            String called = callings[i];
            
            int rank = map.get(called);
            String frontPlayer = players[rank - 1];
            
            players[rank - 1] = called;
            players[rank] = frontPlayer;
            
            map.put(called, rank - 1);
            map.put(frontPlayer, rank);
        }
        
       return players;
    }
}