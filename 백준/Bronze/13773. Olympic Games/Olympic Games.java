import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n;
		while(true) {
			n = Integer.parseInt(br.readLine());
			if(n==0) break;
			if(n==1916||n==1940||n==1944) {
				sb.append(n+" Games cancelled\n");
			}else if(n%4==0&&n>=1896) {
				if(n<=2020) {
					sb.append(n+" Summer Olympics\n");
				}else {
					sb.append(n+" No city yet chosen\n");
				}
			}else {
				sb.append(n+" No summer games\n");
			}
		}
		System.out.println(sb);
	}
}