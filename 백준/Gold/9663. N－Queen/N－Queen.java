import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static int count = 0; // 가능한 경우의 수 저장

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] board = new int[n]; // 체스판 행마다 하나의 퀸 위치 저장
        solve(n, 0, board);

        System.out.println(count); // 가능한 경우의 수 출력
    }

    public static void solve(int n, int row, int[] board) {
        if (row == n) { // 모든 행에 퀸을 놓았을 경우 경우의 수 증가
            count++;
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(row, col, board)) {
                board[row] = col; // 현재 위치에 퀸 놓기
                solve(n, row + 1, board); // 다음 행으로 이동
            }
        }
    }

    public static boolean isSafe(int row, int col, int[] board) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || Math.abs(board[i] - col) == row - i) {
                return false; // 같은 열에 있거나, 대각선에 위치할 경우 불가능
            }
        }
        return true;
    }
}