import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			
		int n = Integer.parseInt(br.readLine());
		int prime[] = new int[n];
		int count = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i = 0 ; i < n; i++) {	
			prime[i] = Integer.parseInt(st.nextToken());
			if(isPrime(prime[i]))
				count++;
		}
		System.out.println(count);
	}
	static boolean isPrime(int n) {
		boolean check = true;
		if(n == 1) check = false;
		else {
			for(int i = 2; i < n; i++) {
				if(n%i == 0)
					check = false;
			}
		}
		
		return check;
	}
}