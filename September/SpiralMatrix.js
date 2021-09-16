// Solution 1

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
 var spiralOrder = function(matrix) {   
    
    if (matrix.length === 1) return matrix[0]
    
    let output = []
    let x = 0
    let y = 0
    
    let maxRight = matrix[0].length - 1
    let maxLeft = 0
    let maxUp = 1
    let maxDown = matrix.length - 1
    
    const maxQtd = matrix.length * matrix[0].length
    
    let dir = maxRight === 0 ? 'down' : 'right'
    // 'right '-> 'down' -> 'left' -> 'up' -> 'right' -> ...
    
    while(output.length < maxQtd) {
        output.push(matrix[x][y])
        switch (dir) {
          case 'right':
            y += 1
            if (y === maxRight) {
                maxRight -= 1
                dir = 'down'
            }
            break;
          case 'down':
            x += 1
            if (x === maxDown) {
                maxDown -= 1
                dir = 'left'
            }
            break;
          case 'left':
            y -= 1
            if (y === maxLeft) {
                maxLeft += 1
                dir = 'up'
            }
            break;
          case 'up':
            x -= 1
            if (x === maxUp) {
                maxUp += 1
                dir = 'right'
            }
            break;
        }
    }
    return output
};

// Solution 2

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
 var spiralOrder2 = function(matrix) {   
    
    if (matrix.length === 1) return matrix[0]
    
    let output = []
    
    let top = 0
    let bottom = matrix.length - 1
    let right = 0
    let left = matrix[0].length - 1
    
    const maxQtd = matrix.length * matrix[0].length
    
    while(output.length < maxQtd) {
        
        for (let i = right; i <= left && output.length < maxQtd; i++){
            output.push(matrix[top][i])
        }
        top += 1
        
        for (let i = top; i <= bottom && output.length < maxQtd; i++){
            output.push(matrix[i][left])
        }
        left -= 1
        
        for (let i = left; i >= right && output.length < maxQtd; i--){
            output.push(matrix[bottom][i])
        }
        bottom -= 1
        
        for (let i = bottom; i >= top && output.length < maxQtd; i--){
            output.push(matrix[i][right])
        }
        right += 1
    }
    return output
};