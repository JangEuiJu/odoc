import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Set;

public class Main {

    static Set<String> set = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) set.add(br.readLine());

        int m = Integer.parseInt(br.readLine());
        while (m-- > 0) {
            String s = br.readLine();
            sb.append(set.contains(s) ? "1\n" : contains(s) ? "2\n" : "0\n");
        }

        bw.write(sb.toString());
        bw.flush();
    }

    private static boolean contains(String s) {
        for (int i = 1; i < s.length(); i++)
            if (set.contains(s.substring(0, i)) && set.contains(s.substring(i))) return true;

        return false;
    }

}