import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		for(int i = 0; i < n; i++) {
			String str = br.readLine();
			int result = 0;
			int ox = 0;
			if(str.charAt(0) == 'O') {ox++; result += 1;}
			for(int j = 1; j < str.length(); j++) {
				if(str.charAt(j) == 'O' && str.charAt(j-1) == 'O') {
					ox++;
					result += ox;
				}
				else if(str.charAt(j) == 'O') {
					ox++;
					result += ox;
				}
				else 
					ox = 0;
			}
			System.out.println(result);
		}
	}
}