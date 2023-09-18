import java.util.*;
import java.io.*;
;public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		Stack<Integer> s = new Stack<>();
		
		int n = Integer.parseInt(br.readLine());
		int start = 0;
		while(n-- > 0) {
			int value = Integer.parseInt(br.readLine());
			
			if(start < value) {
				for(int i=start+1; i<=value; i++) {
					s.push(i);
					sb.append("+\n");
				}
				start = value;
			}
			else if(s.peek() != value) {
				System.out.println("NO");
				System.exit(0);
			}
			s.pop();
			sb.append("-\n");
		}
		System.out.println(sb);
	}
}