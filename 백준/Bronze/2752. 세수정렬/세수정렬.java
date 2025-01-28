import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numbers = new int[3];
        for(int i = 0; i < 3; i++){
            numbers[i] = sc.nextInt();
        }
        
        Arrays.sort(numbers);
        
        for(int i = 0; i < 3; i++){
            System.out.print(numbers[i] + " ");
        }
    }
}