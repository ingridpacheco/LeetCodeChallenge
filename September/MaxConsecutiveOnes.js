// Given a binary array nums, return the maximum number of consecutive 1's in the array.
// Input: nums = [1,1,0,1,1,1]
// Output: 3

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let seq = 0
    return nums.reduce((acc, value) => {
        seq = (value === 1) ? seq + 1 : 0
        if (seq > acc) acc = seq
        return acc
    }, 0)
};