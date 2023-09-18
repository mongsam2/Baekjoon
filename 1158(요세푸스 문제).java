import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) {
		CircularLinkedList cll = new CircularLinkedList(); // 원형 연결리스트
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder(); // 최종 출력 문자열
		int n = sc.nextInt();
		int k = sc.nextInt();
		for (int i=1; i<=n; i++) { // n개의 숫자를 원형 연결리스트에 저장
			cll.insert(i);
		}
		sb.append("<"); // 문자열 시작기호

		// 모든 숫자를 꺼낼 때까지 k만큼 회전하고 숫자를 제거
		for (int i=0; i<n; i++) {
			cll.rotate(k);
			if (i==n-1) { // 마지막 숫자라면 ',' 없이 StringBuilder에 저장
				sb.append(cll.delete());
			}
			else {
				sb.append(cll.delete()).append(", ");
			}
		}
		sb.append(">"); // 문자열 마지막 기호
		System.out.println(sb);
		sc.close();
	}
	
}

/*원형 연결리스트 구현:
 * 노드: 정수 데이터, 다음 노드를 가리키는 노드 변수
 * Node(int data): 정수 데이터를 가진 노드를 만드는 생성자
 * getData(): 노드의 데이터를 반환
 * setNext(Node node): 노드의 다음 노드를 설정
 * getNext(): 다음 노드를 반환
 * 
 * 원형 연결리스트: 
 * tail: 연결리스트의 마지막을 저장하는 변수
 * size: 연결리스트의 길이를 저장하는 변수
 * insert(int data): 정수데이터를 리스트에 추가*
 * delete(): 맨 앞에 있는 노드의 data를 반환하고 노드를 제거
 * rotate(int count): 입력된 정수만큼 리스트를 회전한다.*/

class CircularLinkedList {
	class Node {
		private int data;
		private Node next;
		
		public Node(int data) {
			this.data = data;
			this.next = null;
		}
		public int getData() {
			return data;
		}
		public void setNext(Node n) {
			next = n;
		}
		public Node getNext() {
			return next;
		}
	}
	
	private Node tail;
	public int size;
	
	public CircularLinkedList() {
		tail=null;
		size=0;
	}
	public void insert(int d) {
		Node n = new Node(d);
		if (size==0) {
			tail=n;
			tail.setNext(tail);
		}
		else {
			n.setNext(tail.getNext());
			tail.setNext(n);
			tail=n;
		}
		size++;
	}
	public int delete() {
		int ans=0;
		if (size == 1) {
			ans = tail.getData();
			tail = null;
		}
		else {
			Node del_n = tail.getNext();
			ans = del_n.getData();
			tail.setNext(del_n.getNext());
		}
		size--;
		return ans;
	}
	public void rotate(int c) {
		for (int i=1; i<c; i++) {
			tail = tail.getNext();
		}
	}
}