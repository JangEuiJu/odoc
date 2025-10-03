import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int[] inputs = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			inputs[i] = Integer.parseInt(st.nextToken());
		}
		
		bubbleSort(N, K, inputs);
	}

	private static void bubbleSort(int N, int K, int[] inputs) {
		int cnt = 0;
		
		for (int i = 0; i < N - 1; i++) {
			for (int j = 0; j < N - 1; j++) {
				if (inputs[j] > inputs[j + 1]) {
					swap(inputs, j, j + 1);
					cnt++;
				}
				
				if (cnt >= K) {
					System.out.printf("%d %d", inputs[j], inputs[j + 1]);
					return;
				}
			}
			
		}
		
		System.out.println(-1);
	}

	private static void swap(int[] arr, int i, int j) {
		int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
	}
}