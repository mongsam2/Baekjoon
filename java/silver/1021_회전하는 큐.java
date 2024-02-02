/*
 int N, M = input() // 큐에 처음에 포함되어 있던 수 N(50이하), 뽑아내려고 하는 수의 개수 M(N이하)
 int[] numbers = input() // 뽑아내려고 하는 수의 위치(1이상 N이하)
output: numbers를 뽑아내는데 필요한 로테이션 연산의 최소값
 
 ArrayList<> queue = new ArrayList<Integer>();
 int minRotate = 0
 int pointer = 0
 for number in numbers:
 	nextIndex = queue.indexOf(number)
 	int distance = Math.abs(nextIndex-pointer)
 	if distance <= queue.size()//2
 		minRotate = minRotate + distance
 	else
 		minRotate = minRotate + queue.size() - distance
 	pointer = nextIndex
 	pop()
 print(minRotate)
 
 
 void pop() {
 	if pointer == queue.size()-1
 		queue.remove(pointer)
 		pointer = 0
 	else
 		queue.remove(pointer)
 }
 
 *** Scanner와 BufferedReader를 같이 사용하면 런타임 에러가 발생!!
 */
import java.util.*;
import java.io.*;
public class Main {
	
	public static void main(String[] args) throws IOException{
		ArrayList<Integer> queue = new ArrayList<>(); // ArrayList를 이용해서 순환 queue 구현
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st1.nextToken());
		int m = Integer.parseInt(st1.nextToken());
		
        // 뽑아야 하는 수를 numbers 배열에 저장
        int[] numbers = new int[m];
        StringTokenizer st2 = new StringTokenizer(br.readLine());
		for(int i=0; i<m; i++) {
			numbers[i] = Integer.parseInt(st2.nextToken())-1;
		}

        // 수열을 순환 queue에 저장
		for(int i=0; i<n; i++) {
			queue.add(i);
		}
		
		int minRotate = 0; // 출력값
		int pointer = 0; // 현재 queue 헤더의 위치
        // 뽑아야 하는 숫자들을 순서대로 확인
		for(int i=0; i<m; i++) {
			int number = numbers[i]; // 뽑아야 하는 수
			int nextIndex = queue.indexOf(number); // queue에서 뽑아야 하는 수가 있는 위치
			// 왼쪽으로 로테이션했을 때, 오른쪽으로 로테이션 했을 때의 연산횟수를 비교 후 더 적은 방법을 선택
            int distance = Math.abs(nextIndex-pointer);
			if (distance <= queue.size()/2) {
			 		minRotate = minRotate + distance;
			}
			else {
			 		minRotate = minRotate + queue.size() - distance;
			}
			pointer = nextIndex; // 로테이션을 통해 pointer를 뽑아야하는 숫자가 있는 곳까지 이동
			if(queue != null) {
				queue.remove(pointer); // pointer가 가르키고 있는 숫자를 삭제
				if(pointer > queue.size()) // 숫자를 삭제 후 pointer가 queue의 길이를 넘어간다면 위치를 조정해준다.(맨 끝에 있는 숫자를 삭제했을 경우)
					pointer = 0;
			}
		}
		System.out.println(minRotate);
	}
	
	
}
