class Solution {
    public int solution(int[][] dots) {
        if (isParallel(dots[0], dots[1], dots[2], dots[3])) return 1;
        if (isParallel(dots[0], dots[2], dots[1], dots[3])) return 1;
        if (isParallel(dots[0], dots[3], dots[1], dots[2])) return 1;
        
        return 0;
    }

    private boolean isParallel(int[] a, int[] b, int[] c, int[] d) {
        double slope1 = (double) (b[1] - a[1]) / (b[0] - a[0]);
        double slope2 = (double) (d[1] - c[1]) / (d[0] - c[0]);
        
        return slope1 == slope2;
    }
}
