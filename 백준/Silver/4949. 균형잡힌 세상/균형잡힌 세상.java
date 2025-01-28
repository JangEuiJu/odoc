import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
		Stack<Character> st = new Stack<>();

		while(true) {
			boolean check = true;
			char temp1, temp2;
			String str = br.readLine();
            
            if(str.equals(".")) break;
			
			for(int i = 0; i < str.length(); i++) {
				temp1 = str.charAt(i);
				switch(temp1) {
				case '(': case '[':
					st.push(temp1);
					break;
				case ']': case ')':
					if(st.isEmpty())
						check = false;
					else{
						temp2 = st.pop();
						if((temp2 == '(' && temp1 != ')') ||(temp2 == '[' && temp1 != ']'))
							check = false;
					}		
					break;
				}
			}
			if(!st.isEmpty()) check = false;
			
			if(check)
				System.out.println("yes");
			else
				System.out.println("no");
			st.clear();
		}
	}
}