// Solução 1

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 var intersect = function(nums1, nums2) {
    indexes = {}
    return nums1.reduce((acc, value, index) => {
        if (nums2.includes(value)) {
            if (indexes[value] === undefined) {
                indexes[value] = [nums2.indexOf(value)]
                acc.push(value)
            }
            else {
                const lastIndex = indexes[value][indexes[value].length - 1]
                const newIndex = nums2.indexOf(value, lastIndex + 1)
                if (newIndex !== -1) {
                    indexes[value].push(newIndex)
                    acc.push(value)
                }
            }
        }
        return acc
    }, [])
};

// Solução 2

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 var intersect = function(nums1, nums2) {
    indexes = {}
    
    if (nums2.length === 1){
        return nums1.includes(nums2[0]) ? [nums2[0]] : []
    }
    
    if (nums1.length === 1){
        return nums2.includes(nums1[0]) ? [nums1[0]] : []
    }
    
    return nums1.filter((value) => {
        if (nums2.includes(value)) {
            if (indexes[value] === undefined) {
                indexes[value] = [nums2.indexOf(value)]
                return true
            }
            else {
                const lastIndex = indexes[value][indexes[value].length - 1]
                const newIndex = nums2.indexOf(value, lastIndex + 1)
                if (newIndex !== -1) {
                    indexes[value].push(newIndex)
                    return true
                }
            }
        } 
        return false
    })
};