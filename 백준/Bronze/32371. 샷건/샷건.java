import java.io.*;
import java.util.*;

public class Main {

	static boolean[][] visit; 
	static int[] dx = {-1, 0, 1, -1, 0, 1, -1, 0, 1}; 
	static int[] dy = {-1, -1, -1, 0, 0, 0, 1, 1, 1}; 
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		char[][] key = new char[4][10];
		visit = new boolean[4][10];
		
		for (int i = 0; i < 4; i++) {
			key[i] = br.readLine().toCharArray();
		}
		
		char[] str = br.readLine().toCharArray();
		boolean check; 
		
		for (int i = 0; i < 9; i++) {
			check = false;
			
			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 10; k++) {
					if (key[j][k] == str[i]) { 
						visit[j][k] = true;
						check = true;
						break;
					}
				}
				if (check) {
					break;
				}
			}
		}
		
		char result = ' ';
		for (int i = 1; i < 3; i++) {
			for (int j = 1; j < 9; j++) {
				if (exploration(i, j)) {
					result = key[i][j];
					break;
				}
			}
			
			if (result != ' ') {
				break;
			}
		}
		
		bw.write(result);
		bw.flush();
		bw.close();
		br.close();
	}
	private static boolean exploration (int y, int x) {
		boolean check = true;
		
		for (int i = 0; i < 9; i++) {
			if (!visit[y + dy[i]][x + dx[i]]) {
				check = false;
				break;
			}
		}
		
		return check;
	}
}