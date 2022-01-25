
var RandomizedSet = function() {
    this.set = []
};

function get_random (list) {
    return list[Math.floor((Math.random()*list.length))];
}

/** 
  * @param {number} val
  * @return {boolean}
  */
RandomizedSet.prototype.insert = function(val) {
    if (!this.set.includes(val)) {
        this.set.push(val)
        return true
    }
    return false
};

/** 
  * @param {number} val
  * @return {boolean}
  */
RandomizedSet.prototype.remove = function(val) {
    if (this.set.includes(val)) {
        const indexVal = this.set.indexOf(val)
        this.set.splice(indexVal,1)
        return true
    }
    return false
};

/**
  * @return {number}
  */
RandomizedSet.prototype.getRandom = function() {
    return get_random(this.set)
};

/** 
  * Your RandomizedSet object will be instantiated and called as such:
  * var obj = new RandomizedSet()
  * var param_1 = obj.insert(val)
  * var param_2 = obj.remove(val)
  * var param_3 = obj.getRandom()
  */