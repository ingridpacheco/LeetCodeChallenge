# input => tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# output => 2

# input => tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# output => -1

# input => [1,2,1,1,1,2,2,2] ; [2,1,2,2,2,2,2,2]
# output => 1

# input => [1,2,3,4,6] ; [6,6,6,6,5]
# output => 1

# input => [2,1,1,3,2,1,2,2,1] ; [3,2,3,1,3,2,3,3,2]
# output => -1

def solution1(tops, bottoms):
    top = {}
    bottom = {}
    quantity = {}
    
    if tops[0] == tops[1]:
        top[tops[0]] = 0
        if bottoms[0] == tops[0] or tops[1] == bottoms[1]:
            bottom[tops[0]] = 1
        else:
            bottom[tops[0]] = 2
        quantity[tops[0]] = 2
    else:
        if tops[0] == bottoms[1]:
            bottom[tops[0]] = 1
            top[tops[0]] = 1
            quantity[tops[0]] = 2
        if tops[1] == bottoms[0]:
            bottom[tops[1]] = 1
            top[tops[1]] = 1
            quantity[tops[1]] = 2
    if bottoms[0] == bottoms[1]:
        if bottoms[0] == tops[0] or tops[1] == bottoms[1]:
            top[bottoms[0]] = 1
        else:
            top[bottoms[0]] = 2
        bottom[bottoms[0]] = 0
        quantity[bottoms[0]] = 2
    
    if len(top) == 0 and len(bottom) == 0:
        return -1
    
    for i in range(2,len(tops)):   
        if tops[i] not in top and tops[i] not in bottom and bottoms[i] not in top and bottoms[i] not in bottom:
            return -1
        if bottoms[i] != tops[i]:
            if tops[i] in quantity:
                quantity[tops[i]] += 1
            if bottoms[i] in quantity:
                quantity[bottoms[i]] += 1
            if tops[i] in bottom:
                bottom[tops[i]] += 1
            if bottoms[i] in top:
                top[bottoms[i]] += 1
        else:
            quantity[tops[i]] += 1
        
    min_rotation = -1
    for k in bottom.keys():
        if quantity[k] >= len(tops):
            if min_rotation == -1:
                min_rotation = bottom[k]
            elif bottom[k] < min_rotation:
                min_rotation = bottom[k]
            
    for k in top.keys():
        if quantity[k] >= len(tops):
            if min_rotation == -1:
                min_rotation = top[k]
            elif top[k] < min_rotation:
                min_rotation = top[k]
        
    return min_rotation


if __name__ == "__main__":
    solution1()