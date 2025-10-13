import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] convertTable = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] revertTable = new int[convertTable.length];
        for (int i = 0; i < convertTable.length; i++) {
            revertTable[convertTable[i]] = i;
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        int convertedA = Integer.parseInt(st.nextToken());
        int convertedB = Integer.parseInt(st.nextToken());

        int revertedA = 0, revertedB = 0;
        for (int mul = 1; convertedA > 0; mul *= 10) {
            revertedA += revertTable[convertedA % 10] * mul;
            convertedA /= 10;
        }
        for (int mul = 1; convertedB > 0; mul *= 10) {
            revertedB += revertTable[convertedB % 10] * mul;
            convertedB /= 10;
        }

        int revertedSum = revertedA + revertedB;
        int convertedSum = 0;
        for (int mul = 1; revertedSum > 0; mul *= 10) {
            convertedSum += convertTable[revertedSum % 10] * mul;
            revertedSum /= 10;
        }

        bw.write(Integer.toString(convertedSum));
        bw.flush();

        br.close();
        bw.close();
    }
}