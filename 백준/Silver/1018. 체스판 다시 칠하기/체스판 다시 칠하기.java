import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static boolean[][] board;
	public static int min = 64;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int n = Integer.parseInt(st.nextToken());	
		int m = Integer.parseInt(st.nextToken());
		board = new boolean[n][m];

		for(int i = 0; i < n; i++) {
			String str = br.readLine();
			for(int j = 0; j < m; j++) {
				if(str.charAt(j) == 'W')
					board[i][j] = true;
				else
					board[i][j] = false;
			}
		}
		
		int row = n - 7;
		int col = m - 7;
		
		for(int i = 0; i < row; i++) {
			for(int j = 0; j < col; j++) {
				find(i, j);
			}
		}
		System.out.println(min);
	}
	public static void find(int x, int y) {
		int endX = x + 8;
		int endY = y + 8;
		int count = 0;
		
		boolean TF = board [x][y];
		for(int i = x; i < endX; i++) {
			for(int j = y; j < endY; j++) {
				if(board[i][j] != TF) 
					count++;
				TF = (!TF);
			}
			TF = !TF;
		}
		count = Math.min(count, 64 - count);
		min = Math.min(min, count);
	}
}