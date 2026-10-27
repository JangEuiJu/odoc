class Solution {
    public String solution(String polynomial) {
        int xCount = 0;
        int numCount = 0;

        for (String s : polynomial.split(" \\+ ")) {
            if (s.contains("x")) {
                if (s.length() == 1) {
                    xCount += 1;
                } else {
                    xCount += Integer.parseInt(s.substring(0, s.length() - 1));
                }
            } else {
                numCount += Integer.parseInt(s);
            }
        }

        StringBuilder sb = new StringBuilder();

        if (xCount > 0) {
            if (xCount == 1) {
                sb.append("x");
            } else {
                sb.append(xCount).append("x");
            }
        }

        if (numCount > 0) {
            if (sb.length() > 0) {
                sb.append(" + ");
            }
            sb.append(numCount);
        }

        return sb.length() == 0 ? "0" : sb.toString();
    }
}
