import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        solution();
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] hole = new int[N];
        int[] a = new int[M];
        int[] w = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i < N; i++) {
            hole[i] = Integer.parseInt(st.nextToken());
        }


        for (int i=0 ; i < M ; i++) {
            st = new StringTokenizer(br.readLine());
            a[i] = Integer.parseInt(st.nextToken());
            w[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(hole);

        int answer = 0;

        for (int i=0; i < M ; i++) {
            answer = Math.max(Math.abs(binarySearch(hole, 0, N - 1, a[i]) - a[i]) * w[i], answer);
        }

        System.out.println(answer);
    }


    public static int binarySearch(int[] hole, int left, int right, int target) {

        while (left <= right) {

            int mid = (left +  right) / 2;

            if (hole[mid] == target) {
                return target;
            } else if (hole[mid] < target) {
                left = mid + 1;
            } else {
                right = mid -1;
            }
        }

        if (left >= hole.length) {
            return hole[right];
        } else if (right < 0) {
            return hole[left];
        } else {
            int gap1 = Math.abs(target - hole[left]);
            int gap2 = Math.abs(target - hole[right]);
            return gap1 < gap2 ? hole[left] : hole[right];
        }
    }
}