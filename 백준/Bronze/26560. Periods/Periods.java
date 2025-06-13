import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		sc.nextLine();
		for(int i = 0; i < n; i++) {
			String a = sc.nextLine();
			
			if(a.charAt(a.length() - 1) == '.') {
				System.out.println(a);
			}else {
				System.out.println(a + ".");
			}
		}
		sc.close();
	}
}