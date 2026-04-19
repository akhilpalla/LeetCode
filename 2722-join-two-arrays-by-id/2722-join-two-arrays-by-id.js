/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
function join(arr1, arr2) {
    const idToObj = {};
    
    // Load arr1 into map
    for (const item of arr1) {
        idToObj[item.id] = { ...item };
    }
    
    // Merge arr2 (overrides)
    for (const item of arr2) {
        idToObj[item.id] = { ...idToObj[item.id], ...item };
    }
    
    // Extract, sort by id
    return Object.values(idToObj).sort((a, b) => a.id - b.id);
}
