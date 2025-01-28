import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
			Scanner in = new Scanner(System.in);
			int A, B;
			A = in.nextInt();
			B = in.nextInt();
			
			if(A > B)
				System.out.println(">");
			else if (A < B)
				System.out.println("<");
			else
				System.out.println("==");
			
	}

}
