/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    
    if (nums2.length === 1) return [-1]
    
    return nums1.map(num => {
        const index = nums2.indexOf(num)
        if (index !== nums2.length - 1){
            for (let i = index + 1; i < nums2.length; i++) {
                if (nums2[i] > num)
                    return nums2[i]
                }
        }
        return -1
    })
};