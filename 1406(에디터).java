import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		DoublyLinkedList dl = new DoublyLinkedList();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		
		// 문자열을 리스트에 저장
		for (int i=0; i<s.length(); i++) {
			dl.add(s.charAt(i));
		}
		
		int n = Integer.parseInt(br.readLine()); // 명령문의 개수
		for (int i=0; i<n; i++) {
			String comm = br.readLine();
			char edit = comm.charAt(0);
			// 명령 수행
			if (edit=='L')
				dl.L();
			else if (edit=='D')
				dl.D();
			else if (edit=='B')
				dl.B();
			else
				dl.P(comm.charAt(2));
		}
		dl.show(); // 최종 문자열 출력
		
	}
}

/*양방향 연결 리스트
 * 가장 왼쪽의 노드는 빈 노드
 * cursor: 실제 커서의 왼쪽 글자를 가르킴 / 노드(cursor) |
 * L: 왼쪽 한 칸 옮김(커서가 가장 앞의 노드면 예외 처리)
 * D: 오른쪽 한 칸 옮김 (커서가 가장 뒤의 노드면 예외 처리)
 * B: 기존 커서 노드를 삭제, 새 커서는 왼쪽 노드로 변경 (커서가 맨 앞의 노드면 예외 처리)
 * 커서가 오른쪽 끝일 때: 커서 왼쪽 노드의 오른쪽을 지움->새 커서는 왼쪽 노드로 변경
 * P $: 커서의 오른쪽에 $문자를 데이터로 하는 새 노드를 추가, 새 노드를 커서로 바꿈
 * 리스트의 끝에 새 노드를 추가할 때는 예외 처리
 * 오른쪽 끝일 때: 커서의 오른쪽에 새 노드 연결->새 노드의 왼쪽에 커서 연결->새 노드를 커서로 바꿈
 * 
 * 생성자: 맨 앞의 빈 노드 head 생성, head를 cursor로 지정
 * add(data): 커서의 오른쪽에 새 노드 연결->새 노드의 왼쪽에 커서 연결*/
class DoublyLinkedList {
	class Node {
		char data;
		Node left;
		Node right;
		Node(char d) {
			data = d;
			left = null;
			right = null;
		}
	}
	Node head;
	Node cursor;
	int count;
	
	DoublyLinkedList() {
		Node n = new Node('0');
		head = n;
		cursor = n;
		count = 0;
	}
	public void add(char data) {
		Node n = new Node(data);
		cursor.right = n;
		n.left = cursor;
		cursor = n;
		count++;
	}
	public void L() {
		if (cursor!=head)
			cursor = cursor.left;
	}
	public void D() {
		if (cursor.right!=null)
			cursor = cursor.right;
	}
	public void B() {
		if (cursor!=head) {
			if (cursor.right==null) {
				cursor.left.right=null;
			}
			else {
				cursor.left.right = cursor.right;
				cursor.right.left = cursor.left;
			}
			cursor = cursor.left;
			count--;
		}
	}
	public void P(char c) {
		Node n = new Node(c);
		if (cursor.right == null) {
			cursor.right = n;
			n.left = cursor;
		}
		else {
			n.right = cursor.right;
			n.left = cursor;
			cursor.right.left = n;
			cursor.right = n;
		}
		cursor = n;
		count++;
	}
	public void show() {
		StringBuilder sb = new StringBuilder();
		Node show = head.right;
		for (int i=0; i<count; i++) {
			sb.append(show.data);
			show = show.right;
		}
		System.out.println(sb);
	}
}