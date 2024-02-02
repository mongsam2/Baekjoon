/*
 순환 연결리스트를 사용해서 양방향 큐를 구현한다. head 포인터가 가르키는 노드는 front, previous 노드는 back이 된다.
          node(head) 
 */

 import java.io.*;
 import java.util.*;
 public class Main {
 
     public static void main(String[] args) throws IOException{
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
         Deque deque = new Deque();
         int n = Integer.parseInt(br.readLine());
         for (int i=0; i<n; i++) {
             StringTokenizer st = new StringTokenizer(br.readLine());
             String operator = st.nextToken();
             switch(operator) { // 스위치 문으로 명령에 맞는 메소드 실행
             case "push_front": deque.pushFront(Integer.parseInt(st.nextToken()));
                 break;
             case "push_back": deque.pushBack(Integer.parseInt(st.nextToken()));
                 break;
             case "pop_front": bw.write(deque.popFront()+"\n");
                 break;
             case "pop_back": bw.write(deque.popBack()+"\n");
                 break;
             case "size": bw.write(deque.size()+"\n");
                 break;
             case "empty": bw.write(deque.empty()+"\n");
                 break;
             case "front": bw.write(deque.front()+"\n");
                 break;
             case "back": bw.write(deque.back()+"\n");
                 break;
             }
         }
         bw.flush();
         bw.close();
         br.close();
     }
     
     
 }
 
 class Deque {
     class Node {
         int item;
         Node previous;
         Node next;
         Node(int item) {
             this.item = item;
             this.previous = null;
             this.next = null;
         }
         int getItem() {
             return this.item;
         }
         void setPrevious(Node n) {
             this.previous = n;
         }
         void setNext(Node n) {
             this.next = n;
         }
     }
     Node head;
     Node tail;
     int length;
     Deque() {
         this.head = null;
         this.tail= null;
         this.length = 0;
     }
     void pushFront(int x) {
         Node pushNode = new Node(x);
         if (length == 0) {
             head = pushNode;
             tail = pushNode;
         }
         else {
             pushNode.setNext(head);
             head.setPrevious(pushNode);
             head = pushNode;
         }
         ++length;
     }
     void pushBack(int x) {
         Node pushNode = new Node(x);
         if (length == 0) {
             head = pushNode;
             tail = pushNode;
         }
         else {
             pushNode.setPrevious(tail);
             tail.setNext(pushNode);
             tail = pushNode;
         }
         ++length;
     }
     int popFront() {
         if (length==0)
             return -1;
         else {
             int output = head.getItem();
             head = head.next;
             length--;
             if (length == 0)
                 tail = null;
             return output;
         }
     }
     int popBack() {
         if (length == 0)
             return -1;
         else {
             int output = tail.getItem();
             tail = tail.previous;
             length--;
             if (length == 0) {
                 head = null;
             }
             return output;
         }
     }
     int size() {
         return length;
     }
     int empty() {
         if (length == 0)
             return 1;
         else
             return 0;
     }
     int front() {
         if (length == 0)
             return -1;
         else
             return head.getItem();
     }
     int back() {
         if (length == 0)
             return -1;
         else
             return tail.getItem();
     }
 }