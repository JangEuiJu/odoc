import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int arr[][] = new int [100][100];
		
		int result = 0;
		
		while(n --> 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int row = Integer.parseInt(st.nextToken());
			int col = Integer.parseInt(st.nextToken());
			for(int i = row; i < row+10; i++) {
				for(int j = col; j < col+10; j++) {
					arr[i][j]++;
				}
			}
		}
		for(int i = 0; i < 100; i++) {
			for(int j = 0; j < 100; j++) {
				if(arr[i][j] != 0)
					result++;
			}
		}
		System.out.println(result);
		
	}
}