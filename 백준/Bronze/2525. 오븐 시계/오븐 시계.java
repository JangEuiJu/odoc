import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int h, m, t;
		h = in.nextInt();
		m = in.nextInt();
		t = in.nextInt();
		
		h += t/60;
		m += t%60;
		
		if(m >= 60) {
			h += 1;
			m -= 60;
		}
		if(h >= 24) {
			h -= 24;
		} 
		System.out.println(h + " " + m);
	}

}
