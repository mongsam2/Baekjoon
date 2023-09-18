import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		Stack s = new Stack();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		for (int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String comm = st.nextToken();
			if (comm.equals("push")) {
				s.push(Integer.parseInt(st.nextToken()));
			}
			else if (comm.equals("pop"))
				bw.write(s.pop()+"\n");
			else if (comm.equals("size"))
				bw.write(s.size()+"\n");
			else if (comm.equals("empty"))
				bw.write(s.empty()+"\n");
			else
				bw.write(s.top()+"\n");
		}
		bw.flush();
		bw.close();
	}
	
}
// **문제를 풀고 다른 사람들의 코드를 보니, 명령어의 개수가 주어지기 때문에 스택을 간단하게 배열로 구현하는게 더 편할 것 같다는 생각이 들었다.**
/*스택
 * 노드
 *  data, next, 
 * top: 스택의 가장 위의 노드를 지정
 * size: 스택의 크기를 저장, push() 실행 시 +1, pop()실행 시 -1
 * push(): 새 노드의 다음 노드를 top으로 설정하고 top을 새 노드로 바꾼다.(스택이 비어있다면 예외)
 * pop(): top을 따로 저장, top을 현재 top의 다음 노드로 바꾼다.(스택의 크기가 1이라면 예외)
 * */
class Stack {
	class Node {
		int data;
		Node next;
		Node(int data) {
			this.data = data;
		}
	}
	
	Node top;
	int size;
	Stack() {
		top = null;
		size=0;
	}
	public void push(int d) {
		Node n = new Node(d);
		if (size==0) {
			top = n;
		}
		else {
			n.next = top;
			top = n;
		}
		size++;
	}
	public int pop() {
		int ans = -1;
		// 함수 실행
		if (size!=0) {
			if (size==1) {
				ans = top.data;
				top=null;
			}
			else {
				ans = top.data;
				top = top.next;
			}
			size--;
		}
		return ans;
	}
	public int size() {
		return size;
	}
	public int empty() {
		if (size==0)
			return 1;
		return 0;
	}
	public int top() {
		if (size==0)
			return -1;
		return top.data;
	}
}