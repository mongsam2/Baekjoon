import java.io.*;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException{
		/*
		 for all x:
		 	Node n = new Node(height, index)
		 	ans=0
		 	while stack != empty:
		 		comp = stack.pop()
		 		if comp.height >= x:
		 			ans = comp.index
		 			stack.push(comp)
		 			stack.push(n)
		 			break
		 		else if x>comp.height:
		 			continue
		 	stringbuilder.append(ans = ' ')
		 	stack.push(n)
		 		
		 	*/
		Stack<Node> s = new Stack<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=1; i<=n; i++) {
			int x = Integer.parseInt(st.nextToken());
			Node node = new Node(x, i);
			int ans = 0;
			while(!(s.isEmpty())) {
				Node comp = s.pop();
				if(comp.height>=x) {
					ans = comp.index;
					s.push(comp);
					break;
				}
			}
			sb.append(String.valueOf(ans)+' ');
			s.push(node);
		}
		System.out.println(sb);
	}
	
}

class Node {
	int height;
	int index;
	Node(int h, int i) {
		height = h;
		index = i;
	}
}