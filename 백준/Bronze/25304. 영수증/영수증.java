import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int total = in.nextInt();
		int type = in.nextInt();
		int sum = 0;
		int product, price;
		for(int i = 0; i < type; i++) {
			product = in.nextInt();
			price = in.nextInt();
			sum += product*price;
		}
		if(sum == total)
			System.out.println("Yes");
		else
			System.out.println("No");
	}

}