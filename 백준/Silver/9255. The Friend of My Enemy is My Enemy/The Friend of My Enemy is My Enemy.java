import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int k = read();
        for (int t = 1; t <= k; t++) {
            int n = read(), m = read();

            Node[] graph = new Node[++n];
            while (n-- > 1) graph[n] = new Node(n);

            while (m-- > 0) {
                int a = read(), b = read();
                graph[a].adj.add(b);
                graph[b].adj.add(a);
            }

            sb.append("Data Set ").append(t).append(":\n");
            for (int i : new TreeSet<>(graph[read()].adj)) sb.append(i).append(" ");
            sb.append("\n\n");
        }

        bw.write(sb.toString());
        bw.flush();
    }

    private static class Node {
        int src;
        List<Integer> adj;

        Node(int src) {
            this.src = src;
            this.adj = new ArrayList<>();
        }
    }

    private static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);

        return n;
    }

}