class Solution {
    public String solution(String letter) {
        String[] morse = {
            ".-", "-...", "-.-.", "-..", ".", "..-.",
            "--.", "....", "..", ".---", "-.-", ".-..",
            "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        };
        
        StringBuilder sb = new StringBuilder();
        String[] tokens = letter.split(" ");
        
        for (String token : tokens) {
            for (int i = 0; i < morse.length; i++) {
                if (morse[i].equals(token)) {
                    sb.append((char) ('a' + i));
                    break;
                }
            }
        }
        
        return sb.toString();
    }
}
