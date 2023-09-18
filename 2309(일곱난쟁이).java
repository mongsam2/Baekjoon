import java.util.*;

public class Main {

	public static void main(String[] args) {
	
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[9]; // 아홉 난쟁이들의 키
		int sum = 0; // 난쟁이 키의 합
		int spy1=-1; // 일곱 난쟁이에 속하지 않는 키 1
		int spy2=-1; // 일곱 난쟁이에 속하지 않는 키 2
		
		// 난쟁이들의 키를 입력받는 단계
		for (int i=0; i<9; i++) {
			int x = sc.nextInt();
			sum = sum + x;
			arr[i] = x;
		}

		// 7 난쟁이들 키의 합이 100이 되는 경우를 탐색하는 과정
		for (int i=0; i<9; i++) {
			for (int j=i+1; j<9; j++) {
				if (sum-arr[i]-arr[j] == 100) {
					spy1 = arr[i]; 
					spy2 = arr[j];
				}
			}
		}
		
		Arrays.sort(arr); // 오름차순으로 출력하기위해 배열 정렬
		
		// 정렬된 배열을 돌면서 값 출력
		// 7 난쟁이에 속하지 않는 사람의 키는 출력하지 않는다.
		for (int i=0; i<9; i++) {
			if (arr[i] == spy1 || arr[i] == spy2)
				continue;
			System.out.println(arr[i]);
		}
		sc.close();
	}

}
