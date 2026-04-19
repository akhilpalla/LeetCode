var jsonStringify = function(object) {
    // Handle null
    if (object === null) {
        return "null";
    }

    // Handle strings
    if (typeof object === 'string') {
        return `"${object}"`;
    }

    // Handle numbers
    if (typeof object === 'number') {
        return object.toString();
    }

    // Handle booleans
    if (typeof object === 'boolean') {
        return object.toString();
    }

    // Handle arrays
    if (Array.isArray(object)) {
        let result = object.map(item => jsonStringify(item)).join(",");
        return `[${result}]`;
    }

    // Handle objects
    if (typeof object === 'object') {
        let keys = Object.keys(object);
        let result = keys.map(key => {
            let val = jsonStringify(object[key]);
            return `"${key}":${val}`;
        }).join(",");
        return `{${result}}`;
    }

    // Return undefined for unsupported types
    return undefined;
};