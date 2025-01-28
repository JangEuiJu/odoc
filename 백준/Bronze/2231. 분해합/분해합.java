import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());	
		int temp = 0;
		
		for(int i = 0; i < n; i++) {
			int wkfltn = 0;
			String str = String.valueOf(i);
			for(int j = 0; j < str.length(); j++) {
				wkfltn += (str.charAt(j)-'0');
			}
			temp = i + wkfltn;
			if(temp == n) {
				System.out.println(i);
				break;
			}
		}
		if(temp != n)
			System.out.println(0);
	}
}