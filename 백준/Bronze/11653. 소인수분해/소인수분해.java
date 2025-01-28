import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack<Integer> st = new Stack<>();

		int n = Integer.parseInt(br.readLine());
		int x = 2;
		
		if(n != 1) {
			while(n > 1) {
				if(n % x == 0) {
					System.out.println(x);
					n = n / x;
				}
				else
					x++;
			}
		}

	}
}