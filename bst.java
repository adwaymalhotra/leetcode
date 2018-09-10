import java.util.List;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;

class Node {
	int val;
	Node left;
	Node right;

	public Node(int v) {
		val = v;
	}
}

class bst {
	public static void main(String[] args) {
		if (args.length == 0) {
			System.out.println("Not enough arguments!");
			return;
		}
		bst solution = new bst();
		solution.driver(args);
	}

	void driver(String[] args) {
		Node n = new Node(5);
		n.left = new Node(3);
		n.right = new Node(7);
		n.left.left = new Node(1);
		n.left.left.right = new Node(2);
		n.right.left = new Node(6);
		n.right.right = new Node(8);

		printPreOrderTree(n);

		switch (args[0]) {
		case "ksumpathscount":
			System.out.println(kSumPathsCount(n, Integer.parseInt(args[1])));
			break;
		case "ksumpaths":
			List<List<Integer>> answer = kSumPaths(n, Integer.parseInt(args[1]));
			for (List<Integer> l : answer) {
				for (int i : l) {
					System.out.print(i + " ");
				}
				System.out.println();
			}
			break;
		default:
			System.out.println("Error while parsing input.");
		}
	}

	void printPreOrderTree(Node node) {
		Queue<Node> q = new LinkedList<>();

		q.add(node);

		Node n = null;
		while (!q.isEmpty()) {
			n = q.remove();
			if (n != null) {
				q.add(n.left);
				q.add(n.right);
				System.out.print(n.val + " ");
			} else System.out.print("null ");
		}
		System.out.println();
	}

	int kSumPathsCount(Node root, int k) {
		return kSumPathsCountHelper(root, k, new ArrayList<Node>());
	}

	int kSumPathsCountHelper(Node root, int k, List<Node> path) {
		if (root == null) return 0;

		int count = 0;

		path.add(root);

		count += kSumPathsCountHelper(root.left, k, path)
		         + kSumPathsCountHelper(root.right, k, path);

		int sum = 0;
		for (int i = path.size() - 1; i >= 0; i--) {
			sum += path.get(i).val;

			if (sum == k) {
				count++;
			}
		}

		path.remove(path.size() - 1);

		return count;
	}


	List<List<Integer>> kSumPaths(Node root, int k) {
		List<List<Integer>> result = new ArrayList<>();
		kSumPathsHelper(root, k, new ArrayList<Node>(), result);

		return result;
	}

	void kSumPathsHelper(Node root, int k, List<Node> path, List<List<Integer>> result) {
		if (root == null) return;

		path.add(root);

		kSumPathsHelper(root.left, k, path, result);
		kSumPathsHelper(root.right, k, path, result);

		int sum = 0;
		for (int i = path.size() - 1; i >= 0; i--) {
			sum += path.get(i).val;

			if (sum == k) {
				result.add(getSubList(path, i));
			}
		}

		path.remove(path.size() - 1);
	}

	List<Integer> getSubList(List<Node> list, int start) {
		List<Integer> result = new ArrayList<>();

		for(int i = start; i<list.size(); i++) {
			result.add(list.get(i).val);
		}

		return result;
	}
}