import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int A, B, C;
		A = input.nextInt();
		B = input.nextInt();
		C = input.nextInt();
		System.out.println((A+B)%C);
		System.out.println(((A%C) + (B%C))%C);
		System.out.println((A*B)%C);
		System.out.println(((A%C) * (B%C))%C);

	}

}
