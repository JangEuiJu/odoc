import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int X = Integer.parseInt(br.readLine());
		int top = 1;
		int bot = 1;
		//입력 받은 숫자가 몇 번째 그룹인지 나타내는 n
		int n = 0; 
		//n번째 그룹일 때, n번째 그룹+그 전까지의 그룹의 분수 총 개수 cnt
		int cnt = 0;
		
		if(X == 1) {
			System.out.println("1/1");
		}
		else {
			while(cnt < X) {
				n++;
				cnt = n*(n+1)/2;
			}
			int num = X-(n-1)*n/2;
			if(n%2 == 0) {
				top = num;
				bot = n-num+1;
			}
			else {
				bot = num;
				top = n-num+1;
			}
			System.out.println(top + "/" + bot);
		}
	}
}