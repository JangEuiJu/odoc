import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		Stack<Integer> stX = new Stack<>();
		Stack<Integer> stY = new Stack<>();
		
		int n =input.nextInt();
		int maxX = -10000, minX = 10000, maxY = -10000, minY = 10000;
		
		for(int i = 0; i < n; i++) {
			int x = input.nextInt();
			int y = input.nextInt();
			stX.push(x);
			stY.push(y);
		}
		for(int i = 0; i < stX.size(); i++) {
			if(stX.get(i) > maxX)
				maxX = stX.get(i);
			if(stX.get(i) < minX)
				minX = stX.get(i);
		}
		for(int i = 0; i < stY.size(); i++) {
			if(stY.get(i) > maxY)
				maxY = stY.get(i);
			if(stY.get(i) < minY)
				minY = stY.get(i);
		}
		System.out.println((maxX-minX)*(maxY-minY));
	}
}