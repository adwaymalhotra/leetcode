import java.lang.Integer;

class Solution {

	public static void main(String[] args) {
		if (args.length == 0) {
			System.out.println("Not enough arguments!");
			return;
		}

		switch (args[0]) {
		case "triplestep":
			System.out.println(triplestep(Integer.parseInt(args[1])));
			break;
		case "sort":
			int[] arr = new int[args.length - 2];
			for (int i = 2; i < args.length; i++) arr[i - 2] = Integer.parseInt(args[i]);
			switch (args[1]) {
			case "insertion":
				printIntArray(insertionsort(arr));
				break;
			case "selection":
				printIntArray(selectionsort(arr));
				break;
			case "bubble":
				printIntArray(bubblesort(arr));
				break;
			default: 
				System.out.println("Error while parsing sort method.");
			}
			break;
		default:
			System.out.println("Error while parsing input.");
		}
	}

	public static int[] insertionsort(int[] arr) {
		int t = -1;
		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = i + 1; j < arr.length; j++) {
				if (arr[i] > arr[j]) {
					t = arr[i];
					arr[i] = arr[j];
					arr[j] = t;
				}
			}
		}

		return arr;
	}

	public static int[] selectionsort(int[] arr) {
		int t = -1, minIndex = -1;

		for (int i = 0; i < arr.length - 1; i++) {
			minIndex = i;
			for (int j = i + 1; j < arr.length; j++) {
				if (arr[j] < arr[minIndex])
					minIndex = j;
			}

			if (i != minIndex) {
				t = arr[i];
				arr[i] = arr[minIndex];
				arr[minIndex] = t;
			}
		}

		return arr;
	}

	public static int[] bubblesort(int[] arr) {
		boolean didSwap = true;
		int temp = -1;
		while (didSwap) {
			didSwap = false;
			for (int i = 1; i < arr.length; i++) {
				if (arr[i] < arr[i - 1]) {
					temp = arr[i];
					arr[i] = arr[i - 1];
					arr[i - 1] = temp;
					didSwap = true;
				}
			}
		}

		return arr;
	}

	public static int triplestep(int n) {

		if (n <= 2) return n;

		int minus3 = 1, minus2 = 1, minus1 = 2, current = 0;

		for (int i = 3; i <= n; i++) {
			current = minus1 + minus2 + minus3;
			minus3 = minus2;
			minus2 = minus1;
			minus1 = current;
		}

		return current;
	}

	public static int magicindex(int[] arr) {
		return -1;
	}

	private static void printIntArray(int[] arr) {
		for (int i : arr) {
			System.out.print(i + ",");
		}
	}
}