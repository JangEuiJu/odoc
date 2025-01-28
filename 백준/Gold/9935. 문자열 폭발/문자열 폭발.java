import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
		StringBuilder sb = new StringBuilder("");
		Stack<Character> stack = new Stack<>();

		String str = br.readLine();
		String bomb = br.readLine();


		for(int i = 0; i < str.length(); i++) {
			stack.push(str.charAt(i));

			if(stack.size() >= bomb.length()) {
				boolean check = true;
				for(int j = 0; j < bomb.length(); j++) {
					if(stack.get(stack.size()-bomb.length()+j) != bomb.charAt(j)) {
						check = false;
						break;
					}
				}
				if(check) {
					for(int j = 0; j <bomb.length(); j++)
						stack.pop();
				}
			}
		}
		int len = stack.size();

		if(stack.isEmpty())
			System.out.println("FRULA");
		else {
			for(int i = 0; i < len; i++) 
				sb.append(stack.get(i));
			System.out.println(sb);
		}
	}
}