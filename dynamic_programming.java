import java.lang.Integer;
import java.util.Random;

class Solution {

	public static void main(String[] args) {
		if (args.length == 0) {
			System.out.println("Not enough arguments!");
			return;
		}

		Solution solution = new Solution();
		solution.runner(args);

		System.out.println();
	}

	public void runner(String[] args) {
		switch (args[0]) {
		case "triplestep":
			System.out.println(triplestep(Integer.parseInt(args[1])));
			break;
		case "primes":
			printPrimeFactors(Integer.parseInt(args[1]));
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
			case "merge":
				printIntArray(mergeSortRunner(arr));
				break;
			case "quick":
				quicksort(arr, 0, arr.length - 1);
				printIntArray(arr);
				break;
			default:
				System.out.println("Error while parsing sort method.");
			}
			break;
		default:
			System.out.println("Error while parsing input.");
		}
	}

	void printPrimeFactors(int n) {
		while (n%2==0) {
			System.out.print("2 ");
			n /= 2;
		}

		for(int i = 3; i <= Math.sqrt(n); i+=2) {
			while (n%i==0) {
				System.out.print(i+" ");
				n/=i;
			}
		}

		if (n>2) System.out.println(n);
		else System.out.println();
	}

	public int[] insertionsort(int[] arr) {
		int x = -1;
		for (int i = 1; i < arr.length; i++) {
			for (int j = i; j > 0; j--) {
				if (arr[j - 1] > arr[j]) {
					swap(arr, j - 1, j);
				} else break;
			}
		}

		return arr;
	}

	public int[] selectionsort(int[] arr) {
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

	public int[] bubblesort(int[] arr) {
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

	public int triplestep(int n) {

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

	public int magicindex(int[] arr) {
		return -1;
	}

	private void printIntArray(int[] arr) {
		for (int i : arr) {
			System.out.print(i + ",");
		}
		System.out.println("\b");
	}

	//Merge Sort

// function to merge two sorted segments into B
	void merge(int[] A, int lo, int mid, int hi, int[] B) {
		int i = lo, j = mid + 1;
		for (int k = lo; k <= hi; k++) {
			if (i <= mid && j <= hi) { //neither segment finished
				if (A[i] <= A[j]) {
					B[k] = A[i]; i++;
				} else {
					B[k] = A[j]; j++;
				}
			} else if (i > mid) { //left segment fin
				B[k] = A[j]; j++;
			} else if (j > hi) { //right segment fin
				B[k] = A[i]; i++;
			}
		}
		for (int k = lo; k <= hi; k++) {
			A[k] = B[k];
		}
	}

// recursive mergesort function
	void mergesort(int[] A, int lo, int hi, int[] B) {
		if (lo == hi) return;

		int mid = (lo + hi) / 2;

		mergesort(A, lo, mid, B);
		mergesort(A, mid + 1, hi, B);

		merge(A, lo, mid, hi, B);
	}

// runner/main/helper function to start the sort
	int[] mergeSortRunner(int[] A) {
		int[] B = new int[A.length];

		mergesort(A, 0, A.length - 1, B);

		return B;
	}

	int partition(int[] A, int lo, int hi) {
		int pivot = (hi + lo) / 2;

		int i = pivot - 1;
		int j = pivot + 1;
		while (i >= 0 && pivot > 0) {
			if (A[i] > A[pivot]) {
				swap(A, i, pivot - 1);
				swap(A, pivot - 1, pivot);
				pivot--;
			}
			i--;
		}

		i = pivot + 1;
		while (j <= hi && pivot < hi) {
			if (A[j] <= A[pivot]) {
				swap(A, j, pivot + 1);
				swap(A, pivot, pivot + 1);
				pivot++;
			}
			j++;
		}

		return pivot;
	}

	void swap(int[] A, int i, int j) {
		int t = A[i];
		A[i] = A[j];
		A[j] = t;
	}

	void quicksort(int[] A, int lo, int hi) {
		if (lo >= hi) return;
		int pivot = partition(A, lo, hi);

		quicksort(A, lo, pivot - 1);
		quicksort(A, pivot + 1, hi);
	}
}