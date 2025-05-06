import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = read();
        int[][] mat = new int[n][2];
        for (int i = 0; i < n; i++) {
            mat[i][0] = read();
            mat[i][1] = read();
        }

        int max = 0, s = 0, e = 0, d;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((d = Math.abs(mat[i][0] - mat[j][0]) + Math.abs(mat[i][1] - mat[j][1])) > max) {
                    max = d;
                    s = i;
                    e = j;
                }
            }
        }

        bw.write((s + 1) + " " + (e + 1));
        bw.flush();
    }

    private static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);

        return n;
    }

}