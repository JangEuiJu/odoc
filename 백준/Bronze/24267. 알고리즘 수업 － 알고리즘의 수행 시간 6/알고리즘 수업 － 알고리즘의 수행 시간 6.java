import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		
		long n = input.nextLong();
		System.out.println((n * (n-1) * (n-2))/6);
		System.out.println(3);
	}
}