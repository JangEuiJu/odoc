import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int x, y;
		for(int i = 1; i <= n; i++) {
			x = in.nextInt();
			y = in.nextInt();
			System.out.println(x+y);
		}
	}

}
