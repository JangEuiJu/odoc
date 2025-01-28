
import java.io.IOException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		int x, y, z;
		while(true) {
			x = input.nextInt();
			y = input.nextInt();
			z = input.nextInt();
			if(x == 0 && y == 0 && z == 0)
				break;
			int max = Math.max(Math.max(x, y), z);
			if((x == max && x >= y+z) || (y == max && y >= x+z) || (z == max && z >= x+y))
				System.out.println("Invalid");
			else {
				if(x == y && y == z)
					System.out.println("Equilateral");
				else if(x != y && y != z && x != z)
					System.out.println("Scalene");
				else
					System.out.println("Isosceles");
			}
			
		}

	}
}