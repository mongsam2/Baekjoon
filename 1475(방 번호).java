import java.util.*;

public class Main {

	public static void main(String[] args) {
		// 1475 방 번호
	/*
        // 빼는 방법
		Scanner sc = new Scanner(System.in);
		int count = 0;
		int[] set = {1,1,1,1,1,1,2,1,1};
		int[] numbers = new int[9];
		String n = sc.next();
		for (int i=0; i<n.length(); i++) {
			int index =  Integer.parseInt(n.substring(i,i+1));
			if (index == 9)
				index = 6;
			if (numbers[index]==0) {
				count ++;
				for (int j=0; j<9; j++)
					numbers[j] = numbers[j] + set[j];
			}
			numbers[index]--;
		}
		System.out.println(count);
		sc.close();
	*/ 
        // 더하는 방법
		Scanner sc = new Scanner(System.in);
		int[] numbers = new int[9]; // 사용한 숫자의 개수를 저장할 배열
		String n = sc.next(); // 방 번호를 문자열로 입력

		// 방 번호를 한 자리씩 돌면서 사용 개수를 계산, 9는 6을 사용한 것으로 계산
		for (int i=0; i<n.length(); i++) {
			int number = Integer.parseInt(n.substring(i,i+1));
			if (number == 9)
				number = 6;
			numbers[number]++;
		}
		int max = 0; // 각 숫자가 필요로하는 세트의 수들 중 가장 큰 수
		for (int i=0; i<9; i++) {
			if (i==6) // 6의 경우 특별하게 처리
				numbers[i] = numbers[i]/2 + numbers[i]%2; 
			max = Math.max(max, numbers[i]);
		}
		System.out.println(max);
		sc.close();
	}
	
}