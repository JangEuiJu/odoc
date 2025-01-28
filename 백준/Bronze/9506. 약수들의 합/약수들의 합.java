
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		StringBuilder sb = new StringBuilder("");


		while(true) {
			int sum = 0;
			int n = input.nextInt();
			if(n == -1)
				break;
			int arr[] = new int[n];
			int index = 0;

			for(int i = 1; i < n; i++) {
				if(n % i == 0) {
					arr[index++] = i;
					sum += i;
				}
			}
			if(n != sum)
				System.out.println(n + " is NOT perfect.");
			else {
				System.out.print(n + " = ");
				for(int i = 0; i < index; i++) {
					if(i == index-1)
						System.out.println(arr[i]);
					else 
						System.out.print(arr[i] + " + ");
				}
			}	
		}
	}

}