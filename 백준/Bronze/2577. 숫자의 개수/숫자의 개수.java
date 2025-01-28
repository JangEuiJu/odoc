import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String result = "";
		int array[] = new int[10];
		int a = Integer.parseInt(br.readLine());
		int b = Integer.parseInt(br.readLine());
		int c = Integer.parseInt(br.readLine());
		int mul = a * b * c;
		
		result += mul;
		
		for(int i = 0; i < result.length(); i++) {
			array[(result.charAt(i)-'0')]++;
		}
		for(int i = 0; i < array.length; i++) {
			System.out.println(array[i]);
		}
	}
}