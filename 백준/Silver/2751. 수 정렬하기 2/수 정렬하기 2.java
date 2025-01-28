import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		ArrayList<Integer> arr = new ArrayList<>();
		
		int N = Integer.parseInt(br.readLine());
		for(int i = 0; i < N; i++) 
			arr.add(Integer.parseInt(br.readLine()));

		Collections.sort(arr);
		
		for(int i = 0; i < N; i++) 
			sb.append(arr.get(i)+"\n");
		
		System.out.println(sb);

	}
}