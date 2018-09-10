class Solution {
    public int jump(int[] nums) {
        
        //keep track of furthest jump possible from current element
        
        //jump end is the last index where we can reach after previous jump
        int current = 0, farthest = 0, count = 0, jumpEnd = 0;
        
        for (int i = 0; i < nums.length-1; i++) {
            farthest = Math.max(farthest, i+nums[i]);
            if (i == jumpEnd) {
                jumpEnd = farthest;
                count++;
            }
        }
        
        return count;
    }
}
