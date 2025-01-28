import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		char[][] arr = new char[5][15];
		
		for(int i = 0; i < 5; i++) {
			String str = input.next();
			for(int j = 0; j < str.length(); j++) {
				arr[i][j] = str.charAt(j);
			}
		}
		
		for(int i = 0; i < 15; i++) {
			for(int j = 0; j < 5; j++) {
				if(arr[j][i] != ' ' && arr[j][i] != '\0')
					System.out.print(arr[j][i]);
			}
		}
		input.close();
	}
}