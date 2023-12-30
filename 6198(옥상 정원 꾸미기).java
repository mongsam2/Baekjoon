 * int n(input): 빌딩의 개수
 * heights[n](input): 빌딩의 높이들
 * ----------------------------------
 * Stack h, cmp
 * 
 * 
 * int count(output): 관리인들이 볼 수 있는 빌딩의 수의 합
 * 
 * 반례: 5 3 3 3 -> 2 스택 cmp에 있는 빌딩들을 꺼내 비교하는 for 문에서 cmp.size() 를 사용하여 오류 발생
 * 
 * 출력값을 저장하는 ans를 int형으로 선언할 경우, 최대 빌딩의 개수가 80,000이기 때문에 출력값을 저장할 수 없음
 * -> long 형으로 선언하여 문제 해결*/

import java.io.*;
import java.util.*;
public class Main {

	public static void main(String[] args) throws IOException{
		Stack<Building> h = new Stack<>(); //빌딩들을 저장
		Stack<Building> cmp = new Stack<>(); // 높이 비교가 필요한 빌딩들을 담은 스택
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// Input
		int n = Integer.parseInt(br.readLine()); //빌딩의 수
        // 스택 h에 빌딩들을 순서대로 쌓는다.
		for(int i=0; i<n; i++) {
			Building bd = new Building(Integer.parseInt(br.readLine()));
			h.push(bd);
		}
		
		cmp.push(h.pop()); // 가장 오른쪽에 있는 빌딩은 아무런 연산도 필요하지 않다.
		
		//Output
		long ans = 0;
		
		// 각 빌딩별로 벤치마킹이 가능한 빌딩의 수를 구하기
		for(int i=1; i<n; i++) {
			Building b = h.pop(); // 벤치마킹 수를 구할 빌딩
			// 높이 비교
			int size = cmp.size(); // cmp 비교의 최대 반복수
			for (int j=0; j<size; j++) {  // cmp의 사이즈를 따로 변수에 저장하지 않고 바로 쓰게 되면 사이즈가 계속 바뀌게 되는 문제가 발생
				Building c = cmp.pop();
				if(b.height > c.height) {
					b.marking = b.marking + 1 + c.marking;
				}
				else {
					cmp.push(c);
					break;
				}
			}
			cmp.push(b);
			ans = ans + b.marking;
		}
		System.out.println(ans);
	}
	
}

// 스택에 넣을 빌딩 객체
class Building {
	int height; //높이
	int marking; // 마킹할 수 있는 빌딩의 수
	Building(int height) {
		this.height = height;
		this.marking = 0;
	}
    // 빌딩 객체를 출력할 경우 height 값을 보여주도록 오버라이딩
	public String toString() {
		return String.valueOf(height);
	}
}