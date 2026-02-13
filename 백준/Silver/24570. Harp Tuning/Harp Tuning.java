import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;

public class Main { 

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String str = bf.readLine();

		String harp = "";
		String number = "";
		for (int i = 0; i < str.length(); i++) {
			if (Character.isAlphabetic(str.charAt(i))) {
				harp += str.charAt(i);
				if (!number.equals("")) {
					bw.write(number + "\n");
					number = "";
				}
			} else {
				if(!harp.equals("")) {
					bw.write(harp + " ");
					harp = "";
				}
				if (Character.isDigit(str.charAt(i))) {
					number += str.charAt(i);
				} else {
					if (str.charAt(i) == '+') {
						bw.write("tighten ");
					} else {
						bw.write("loosen ");
					}
				}
			}
		}
		bw.write(number);
		bw.flush();
	}
}