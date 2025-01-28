import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int result= 5000;
		if(N == 4 || N ==7)
			result = -1;
		else {
			for(int x = 0; x <= N/3; x++) {
				for(int y = 0; y<= N/5; y++) {
					if(3*x + 5*y == N && x+y < result)
						result = x+y;
				}
			}
		}
		System.out.println(result);	
	}
}