/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    let num_points = points.reduce((acc, v) => {
        dist = Math.sqrt(v[0]**2 + v[1]**2)
        if (acc[dist] === undefined){
            acc[dist] = [v]
        }
        else {
            acc[dist].push(v)
        }
        return acc
    },{})
    
    num_points = Object.entries(num_points).sort(function(a, b) {
        return a[0] - b[0];
    });
    
    let index = 0
    let result = []
    
    while (index < k) {
        ar_value = num_points.splice(0,1)
        index += ar_value[0][1].length
        result = result.concat(ar_value[0][1])
    }
    
    return result
};