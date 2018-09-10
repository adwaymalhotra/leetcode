import java.util.Random;

class Practice {

	public static void main(String[] args) {

		Node ll1 = getRandomLL(1, 9, 5);
		Node ll2 = getRandomLL(1, 9, 6);

		printLinkedList(ll1);
		printLinkedList(ll2);

		printLinkedList(addLinkedLists(ll1, ll2));
	}

	public static Node getRandomLL(int lower, int upper, int length) {
		Random rn = new Random();
		Node start = null, last = null;
		while (length > 0) {
			Node n = new Node();
			n.val = lower + rn.nextInt(upper - lower + 1);
			if (start == null) {
				start =  n;
				last = start;
			} else {
				last.next = n;
				last = n;
			}
			length--;
		}
		return start;
	}

	public static void partitionLinkedList(Node head, int p) {
		printLinkedList(head);
		if (head == null) return;

		Node small = null, prev = null, x = head;

		if (x.val < p) {
			small = x;
		}

		prev = x;
		x = x.next;

		while (x != null) {
			if (x.val < p) {
				if (prev == small) {
					small = x;
					prev = x;
					x = prev.next;
				} else if (small == null) {
					prev.next = x.next;
					x.next = head;
					small = x;
					head = x;
				} else {
					prev.next = x.next;
					x.next = small.next;
					small.next = x;
					small = x;
				}
				x = prev.next;
			} else {
				prev = x;
				x = x.next;
			}
		}
		printLinkedList(head);
	}

	public static void printLinkedList(Node n) {
		while (n != null) {
			System.out.print(n.val + "->");
			n = n.next;
		}
		System.out.print("End\n");
	}

	public static Node addLinkedLists(Node ll1, Node ll2) {
		int carry = 0;
		Node p1 = ll1, p2 = ll2, p1prev = null;
		while (p1 != null && p2 != null) {
			int sum = carry + p1.val + p2.val;
			p1.val = sum % 10;
			carry = sum / 10;

			p1prev = p1;
			p1 = p1.next;
			p2 = p2.next;
		}

		if (p1 == null && p2 != null) {
			p1prev.next = p2;
			p1 = p2;
		}

		while (p1 != null) {
			int sum = carry + p1.val;
			p1.val = sum % 10;
			carry = sum / 10;

			p1prev = p1;
			p1 = p1.next;
		}

		if (carry > 0) {
			Node n = new Node();
			n.val = carry;
			p1prev.next = n;
		}

		return ll1;
	}
}

class Node {
	int val = -1;
	Node next;
}