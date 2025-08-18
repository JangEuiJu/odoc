import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine()); 
		char[] str = br.readLine().toCharArray(); 
		
		boolean lastCheck = str[str.length - 1] == 'A' || str[str.length - 1] == 'B' || str[str.length - 1] == 'C' ? true : false; // 마지막이 +, 0, - 가 아니라면 true
		String before = " "; 
		String nowStr = " ";
		char now = ' ';
		char next = ' '; 
		
		for (int i = 0; i < str.length - 1; i++) {
			now = str[i];
			next = str[i + 1];
			
			if (next == '+' || next == '-') {
				nowStr = String.valueOf(now) + String.valueOf(next);
				i++;
			} else if (next == '0') {
				nowStr = String.valueOf(now);
				i++;
			} else {
				nowStr = String.valueOf(now);
				
				if (i == str.length - 2) {
					lastCheck = true;
				}
			}
			
			sb.append(change(nowStr, before));
			before = nowStr; 
		}
		
		if (lastCheck) { 
			sb.append(change(String.valueOf(str[str.length - 1]), before));
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	private static char change(String s, String b) {
		if (s.charAt(0) == 'C') {
			return 'B';
		} else if (s.equals("B") || s.equals("B-")) {
			if (b.charAt(0) == 'C' || b.equals(" ")) {
				return 'D';
			} else {
				return 'B';
			}
		} else if (s.equals("A-") || s.equals("B+")) {
			if (b.equals("B+") || b.charAt(0) == 'A') {
				return 'D';
			} else {
				return 'P';
			}
		} else if (s.equals("A")) {
			if (b.equals("A+") || b.equals("A")) {
				return 'P';
			} else {
				return 'E';
			}
		} else {
			return 'E';
		}
	}
}