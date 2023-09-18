import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // scanner로 배열을 입력받을 시 시간이 오래 걸리는 단점을 보완
		//Scanner sc = new Scanner(System.in);
		int count = 0; // 정수 쌍의 개수
		int n = Integer.parseInt(br.readLine()); // 수열의 크기입력
		StringTokenizer st = new StringTokenizer(br.readLine()); // 수열 입력
		int x = Integer.parseInt(br.readLine()); // x입력
		int[] arr = new int[n]; // 수열을 담을 배열
		
		// 정수 n개 입력 받기
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr); // 배열 정렬

		int i=0; // 배열의 앞에서 부터 시작하는 인덱스
		int j=n-1; // 배열의 뒤에서 부터 시작하는 인덱스


		while (i < j) { // i와 j가 겹쳐지면 종료
			int sum = arr[i]+arr[j];
			if (sum == x) { // 두 수의 합이 x이면 count를 1증가, i를 1증가시켜서 다른 순서쌍을 찾는다.
				count++;
				i++; // 주의: i의 값을 증가시키지 않으면 i와 j가 정지해있는 상황이 발생하여 반복문이 끝나지 않는다.
			}
			else if (sum < x) // 두 수의 합이 x보다 작으면 i의 값을 증가시켜 sum을 증가시킨다.
				i++;
			else // 두 수의 합이 x보다 크면 j의 값을 감소시켜 sum의 값을 감소시킨다.
				j--;
		}
		System.out.println(count);
		//sc.close();
		
	}
	
}
