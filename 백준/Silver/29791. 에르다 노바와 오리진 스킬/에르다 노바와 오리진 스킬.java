import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		
		int[] ans = new int[n], oss = new int[m];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			ans[i] = Integer.parseInt(st.nextToken());
		}
        st = new StringTokenizer(br.readLine());
		for(int i = 0; i < m; i++) {
			oss[i] = Integer.parseInt(st.nextToken());
		}
        
        Arrays.sort(ans);
		Arrays.sort(oss);
		
        int an = 0, os = 0;
		int ancount = 0, oscount = 0;
        for(int i = 0; i < n; i++){
            if(an == 0) {
				an = ans[i];
				ancount++;
			}
			else {
				if(ans[i] - an >= 100) {
					an = ans[i];
					ancount++;
				}
			}
        }
        for(int i = 0; i < m; i++){
            if(os == 0) {
				os = oss[i];
				oscount++;
			}
			else {
				if(oss[i] - os >= 360) {
					os = oss[i];
					oscount++;
				}
			}
        }
		
		System.out.print(ancount + " " + oscount);
	}
}