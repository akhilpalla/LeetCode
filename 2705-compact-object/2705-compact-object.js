/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (obj === null || typeof obj !== "object") {
        return obj;
    }

    // If it's an array
    if (Array.isArray(obj)) {
        return obj
            .map(item => compactObject(item)) // recurse
            .filter(Boolean); // remove falsy values
    }

    // If it's an object
    const result = {};
    
    for (let key in obj) {
        const value = compactObject(obj[key]); // recurse
        
        if (Boolean(value)) {
            result[key] = value;
        }
    }

    return result;
};