import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine()); // 테스트 케이스
		for (int i=0; i<n; i++) {
			DoublyLinkedList dl = new DoublyLinkedList(); // 연결 리스트 선언
			String s = br.readLine(); // 입력 기록
			for (int j=0; j<s.length(); j++) { // 문자 하나씩 확인하면서 알맞는 메소드 실행
				char c = s.charAt(j);
				
				switch(c) {
				case '-': // 백스페이스
					dl.backspace();
					break;
				case '<': // 왼쪽 화살표
					dl.left();
					break;
				case '>': // 오른쪽 화살표
					dl.right();
					break;
				default: // 문자입력
					dl.insert(c);
				}
					
			}
			dl.show(); // 최종 문자열 출력
		}
	}
	
}

class DoublyLinkedList {
	// insert(data): 문자를 리스트에 추가
	// backspace(): 문자를 지운다.
	// left(): 커서를 왼쪽으로 1칸 이동
	// right(): 커서를 오른쪽으로 1칸 이동
	class Node {
		char data;
		Node left;
		Node right;
		Node(char data) {
			this.data = data;
			left=null;
			right=null;
		}
	}
	Node cursor=null;
	Node head=null;
	int len=0;
	DoublyLinkedList() {
		Node n = new Node('0'); // 맨 앞에 있는 빈 노드
		cursor = n;
		head = n;
	}
	// 커서가 맨 오른쪽 일 때는 노드를 그냥 연결
	// 아니라면 노드들 사이에 연결
	// 길이 1 증가
	public void insert(char data) {
		Node n = new Node(data);
		if (cursor.right==null) {
			cursor.right = n;
			n.left=cursor;
			cursor=n;
		}
		else {
			Node n_right = cursor.right;
			cursor.right=n;
			n_right.left=n;
			n.left=cursor;
			n.right = n_right;
			cursor = n;
		}
		len++;
	}
	// 커서가 가장 왼쪽에 있다면 동작하지 않음
	// 커서가 가장 오른쪽일 때와 아닐 때로 나누어 실행
	// 커서의 왼쪽을 새 커서로 지정
	public void backspace() {
		if (cursor.left!=null) {
			if (cursor.right==null) {
				Node l = cursor.left;
				l.right = null;
				cursor=l;
			}
			else {
				Node l = cursor.left;
				Node r = cursor.right;
				l.right = r;
				r.left = l;
				cursor=l;
			}
			len--;
		}
	}
	// 커서가 왼쪽 끝일 때는 동작하지 않음
	public void left() {
		if (cursor.left!=null) {
			cursor = cursor.left;
		}
	}
	// 커서가 오른쪽 끝일 때는 동작하지 않음
	public void right() {
		if (cursor.right!=null) {
			cursor = cursor.right;
		}
	}
	public void show() {
		Node p = head.right;
		StringBuilder sb = new StringBuilder(); // 긴 문자열을 더하는 상황이 발생할 경우 StringBuilder를 적극적으로 사용하면 좋다.
		for (int i=0; i<len; i++) {
			sb.append(p.data);
			p = p.right;
		}
		System.out.println(sb);
	}
	
}