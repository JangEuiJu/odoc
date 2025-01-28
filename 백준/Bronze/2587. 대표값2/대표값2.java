import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
		
		int sum = 0;
		int av[] = new int[5];
		
		for(int i = 0; i < 5; i++) {
			av[i] = Integer.parseInt(br.readLine());
			sum += av[i];
		}
		Arrays.sort(av);
		
		System.out.println(sum/5);
		System.out.println(av[2]);
		
	}
}