import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int array[] = new int[N];
		st = new StringTokenizer(br.readLine(), " ");
		
		for(int i = 0; i < N; i++) 
			array[i] = Integer.parseInt(st.nextToken());
		
		int result = search(array, N, M);
		
		System.out.println(result);
	}
	
	static int search(int[] arr, int N, int M) {
		int result = 0;
		
		for(int i = 0; i < N-2; i++) {
			for(int j = i+1; j < N-1; j++) {
				for(int k = j+1; k < N; k++) {
					int temp = arr[i] + arr[j] + arr[k];
					if(M == temp) 
						return temp;
					if(temp < M && temp > result)
						result = temp;
				}
			}
		}
		return result;
	}
}
