import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int result = 1;
		int range = 2;
		
		if(N == 1)
			System.out.println(1);
		else {
			while(range <= N) {
				range = range + (6*result);
				result++;
			}
			System.out.println(result);
		}
	}
}