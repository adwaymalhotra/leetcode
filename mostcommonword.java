class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String punctuation = "!?',;. ";
        String p = paragraph.toLowerCase();
        p = p.replaceAll("[!?',;.]", "").trim();
        String[] words = p.split(" ");
        
        Map<String, Integer> counts = new HashMap();
        
        for (String w: words) {
            if (counts.containsKey(w)) {
                counts.put(w, counts.get(w) + 1);
            } else {
                counts.put(w, 1);
            }
        }
        String ans = "";
        int max = 0;
        List<String> b = Arrays.asList(banned);
        for(String key: counts.keySet()) {
            if (!b.contains(key) && counts.get(key)>max) {
                ans = key;
                max = counts.get(key);
            }
        }
        
        return ans;
    }
}