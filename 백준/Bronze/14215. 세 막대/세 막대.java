import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		
		int a = input.nextInt();
		int b = input.nextInt();
		int c = input.nextInt();

		int max = Math.max(Math.max(a,b), c);
		
		if(a+b+c-max > max) System.out.println(a+b+c);
		else System.out.println((a+b+c-max)*2-1);
	}
}