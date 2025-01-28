import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int longNum;
		longNum = n/4;
		for(int i = 0; i < longNum; i++) {
			System.out.print("long ");
		}
		System.out.print("int");
		
	}

}