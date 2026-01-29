import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = read(), m = read();
        int[] arr = new int[n + m + 1];
        for (int i = 1; i <= n; i++) for (int j = 1; j <= m; j++) arr[i + j]++;

        int max = 0;
        for (int i = 1; i < arr.length; i++) max = Math.max(max, arr[i]);
        for (int i = 1; i < arr.length; i++) if (max == arr[i]) sb.append(i).append("\n");

        bw.write(sb.toString());
        bw.flush();
    }

    private static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);

        return n;
    }

}