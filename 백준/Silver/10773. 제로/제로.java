import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
		Stack<Integer> st = new Stack<Integer>();
		
		int k = Integer.parseInt(br.readLine());
		int sum = 0;
		
		for(int i = 0; i < k; i++) {
			int n = Integer.parseInt(br.readLine());
			if(n == 0)
				st.pop();
			else
				st.push(n);
		}
		while(!st.empty())
			sum += st.pop();
		System.out.println(sum);
	}

}