import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int[][] w, p;
	static final int INF = 1000000000;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		
		w = new int[n+1][n+1];
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= n; j++) {
				w[i][j] = INF;
				if(i == j){
					w[i][j] = 0;
				}
			}
		}


		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());

			w[a][b] = Math.min(w[a][b], c); 
		}

		shortPath();
		
		StringBuilder sb = new StringBuilder();
		for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
            	if(w[i][j] == INF) {
            		w[i][j] = 0;
            	}

                sb.append(w[i][j] + " ");
            }
            sb.append("\n");
        }
		System.out.println(sb);
	}

	public static void shortPath() {
		for(int k = 1; k <= n; k++) {
			for(int i = 1; i <= n; i++) {
				for(int j = 1; j <= n; j++) {
					if(w[i][j] > w[i][k] + w[k][j]) 
						w[i][j] = w[i][k] + w[k][j];
				}
			}
		}
	}
}