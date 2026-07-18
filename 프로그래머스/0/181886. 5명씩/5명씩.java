class Solution {
    public String[] solution(String[] names) {
        String[] answer = new String[(names.length + 4) / 5];
        
        for (int i = 0, j = 0; i < names.length; i += 5) 
            answer[j++] = names[i];
        
        return answer;
    }
}