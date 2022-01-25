/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function(nums) {
    return nums.map((num, index) => {
        let biggerIndex = index === nums.length - 1 ? 0 : index + 1
        let smallerIndex = index === 0 ? nums.length - 1 : index - 1
        let greaterIndex = -1
        const rounds = Math.ceil((nums.length - 1) / 2)
        let i = 0
        while(i < rounds) {
            if (nums[biggerIndex] > num) return nums[biggerIndex]
            if (nums[smallerIndex] > num && (greaterIndex === -1 || smallerIndex < greaterIndex) ) {
                greaterIndex = smallerIndex
            }
            biggerIndex = biggerIndex === nums.length - 1 ? 0 : biggerIndex + 1
            smallerIndex = smallerIndex === 0 ? nums.length - 1 : smallerIndex - 1
            i++
        }
        return greaterIndex === -1 ? -1 : nums[greaterIndex]
    })
};