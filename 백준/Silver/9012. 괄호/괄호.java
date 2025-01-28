import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
		Stack<Character> st = new Stack<>();

		int T = Integer.parseInt(br.readLine());
		

		for(int i = 0; i < T; i++) {
			boolean check = true;
			String vps = br.readLine();

			for(int j = 0; j < vps.length(); j++) {
				if(vps.charAt(j) == '(')
					st.push(vps.charAt(j));
				else 
					if(st.isEmpty())
						check = false;
					else
						st.pop();
			}	
			if(!st.isEmpty())
				check = false;
			if(check)
				System.out.println("YES");
			else
				System.out.println("NO");
			
			st.clear();
			
		}
	}
}