import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder("");	

		int m = Integer.parseInt(br.readLine());
		int n = Integer.parseInt(br.readLine());
		int sum = 0;
		int least = 10000;
		for(int i = m; i <= n; i++) {
			if(isPrime(i)) {
				sum+= i;
				if(i < least)
					least = i;
			}
		}
		if(sum == 0) {
			System.out.println(-1);
		}
		else {
			System.out.println(sum);
			System.out.println(least);
		}
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