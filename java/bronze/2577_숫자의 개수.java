/*
 */
import java.util.*;
import java.io.*;
public class Main {
	
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		String result = Integer.toString(a*b*c);
		int[] count = new int[10];
		for (int i=0; i<result.length(); i++) {
			int number = Integer.parseInt(result.substring(i,i+1));
			count[number]++;
		}
		for (int i=0; i<10; i++) {
			System.out.println(count[i]);
		}
		
	}
	
	
}
