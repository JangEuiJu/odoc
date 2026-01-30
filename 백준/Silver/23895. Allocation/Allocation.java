import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int t = read();
        for (int tc = 1; tc <= t; tc++) {
            int n = read(), b = read();
            int[] arr = new int[n];
            while (n-- > 0) arr[n] = read();

            Arrays.sort(arr);

            while (++n < arr.length && arr[n] <= b) b -= arr[n];

            sb.append("Case #").append(tc).append(": ").append(n).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
    }

    private static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);

        return n;
    }

}