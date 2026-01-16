import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String line = br.readLine();
        ArrayList<String> usedVal = new ArrayList<>();

        while (line.contains("for")) {
            String[] val =  line.split(" ");
            if(usedVal.contains(val[2])) usedVal.remove(val[2]);
            usedVal.add(val[2]);
            line = br.readLine().trim();
        }

        Set<String> query = new HashSet<>(Arrays.asList(line.split("")));

        int blank = 0;
        for (int i = 0; i < usedVal.size(); i++) {
            String curVal = usedVal.get(i);
            if (query.contains(curVal)) {

                bw.write(" ".repeat(blank)+"for (int "+curVal+" = 1; "+curVal+" < 9; "+curVal+"++)\n");
                blank++;
                query.remove(curVal);
            };
        }

        bw.write(" ".repeat(blank)+line);

        bw.flush();
        bw.close();
        br.close();
    }
}