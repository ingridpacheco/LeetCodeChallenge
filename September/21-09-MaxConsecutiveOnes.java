// Given a binary array nums, return the maximum number of consecutive 1's in the array.
// Input: nums = [1,1,0,1,1,1]
// Output: 3

class Solution2 {
    public int findMaxConsecutiveOnes(int[] nums) {
        int seq = 0;
        int max_seq = 0;
        for (int i = 0; i < nums.length; i++) {
            seq = (nums[i] == 1) ? seq + 1 : 0;
            if (seq > max_seq) {
                max_seq = seq;
            }
        }
        return max_seq;
    }
}