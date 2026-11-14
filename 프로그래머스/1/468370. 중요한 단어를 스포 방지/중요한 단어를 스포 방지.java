import java.util.*;

class Solution {
    public int solution(String message, int[][] spoiler_ranges) {
        int curIdx = 0;
        List<String> spoilerWords = new ArrayList<>();
        Set<String> noSpoilerWords = new HashSet<>();
        for (String word : message.split(" ")) {
            int start = message.indexOf(word, curIdx);
            int end = start + word.length() - 1;
            curIdx = end + 1;
            boolean isSpoiler = false;
            for (int[] range: spoiler_ranges) {
                if (start <= range[1] && end >= range[0]) {
                    spoilerWords.add(word);
                    isSpoiler = true;
                    break;
                }
            }
            if (!isSpoiler) {
                noSpoilerWords.add(word);
            }
        }
        Set<String> importantWords = new HashSet<>();
        for (String spoilerWord : spoilerWords) {
            if (!importantWords.contains(spoilerWord) && 
                    !noSpoilerWords.contains(spoilerWord)) {
                importantWords.add(spoilerWord);
            }
        }
        return importantWords.size();
    }
}