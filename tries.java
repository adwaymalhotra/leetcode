class Trie {
    TrieNode root = new TrieNode('#');
    
    /** Initialize your data structure here. */
    public Trie() {
        
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        root.addWord(word);
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        return root.searchChildren(word);
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        return root.startsWith(prefix);
    }
}

class TrieNode {
    char c = '#';
    boolean hasEnd = false;
    TrieNode[] children = new TrieNode[26];
    // Map<Character, TrieNode> children = new HashMap<>();
    
    public void addWord(String word) {
        if (word.length() == 0) {
            hasEnd = true;
            return;
        }
        char c = word.charAt(0);
        if (children[c-'a'] != null) {
            children[c-'a'].addWord(word.substring(1));
        } else {
            TrieNode node = new TrieNode(c);
            children[c-'a'] = node;
            node.addWord(word.substring(1));
        }
    }
    
    public TrieNode(char c) {
        this.c = c;
    }
    
    public boolean startsWith(String word) {
        if (word.length() == 0) return true;
        
        char c = word.charAt(0);
        
        if (children[c-'a'] != null) {
            return children[c-'a'].startsWith(word.substring(1));
        }
        
        return false;
    }
    
    public boolean searchChildren(String word) {
        if (word.length() == 0) return hasEnd;
        
        char c = word.charAt(0);
        
        if (children[c-'a'] != null) {
            return children[c-'a'].searchChildren(word.substring(1));
        }
            
        return false;
    }
}