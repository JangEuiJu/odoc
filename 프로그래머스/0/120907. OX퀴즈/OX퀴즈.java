class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        
        for (int i = 0; i < quiz.length; i++) {
            String[] temp = quiz[i].split(" ");
            int x = Integer.parseInt(temp[0]);
            int y = Integer.parseInt(temp[2]);
            int z = Integer.parseInt(temp[4]);
            String op = temp[1];
            
            int calc = 0;
            if (op.equals("+")) {
                calc = x + y;
            } else {
                calc = x - y;
            }
            
            if (calc == z) {
                answer[i] = "O";
            } else {
                answer[i] = "X";
            }
        }
        
        return answer;
    }
}
