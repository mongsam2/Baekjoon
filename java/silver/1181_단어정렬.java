/*
 */
import java.util.*;
import java.io.*;
public class Main {
	
	public static void main(String[] args) throws IOException{
		ArrayList<String> arr = new ArrayList<>();
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		for(int i=0; i<n; i++) {
			arr.add(br.readLine());
		}
		new_Comparator c = new new_Comparator();
		arr.sort(c);
		sb.append(arr.get(0)+"\n");
		for(int i=1; i<n; i++) {
			if(arr.get(i).equals(arr.get(i-1)))
				continue;
			sb.append(arr.get(i)+"\n");
		}
		System.out.println(sb);
	}
	
	
}

class new_Comparator implements Comparator<String> {
	public int compare(String s1, String s2) {
		if(s1.length() > s2.length()) {
			return 1;
		}
		else if(s1.length() < s2.length()) {
			return -1;
		}
		return s1.compareTo(s2);
	}
}
