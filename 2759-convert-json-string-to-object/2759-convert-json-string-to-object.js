const STACK_ENTRY_TYPE = {
  OBJECT: 1,
  ARRAY: 2,
}

function createNewObjectEntry() {
    return {
        type: STACK_ENTRY_TYPE.OBJECT,
        data: {},
        fieldName: undefined,
    }
}

function createNewArrayEntry() {
    return {
        type: STACK_ENTRY_TYPE.ARRAY,
        data: [],
    }
}

var jsonParse = function(str) {
    const stack = [];
    let i = 0;
    const n = str.length;
    let result = undefined;

    const useValue = (value) => {
        if (!stack.length) {
            result = value;
            return;
        }
        const top = stack[stack.length - 1];
        if (top.type === STACK_ENTRY_TYPE.OBJECT) {
            top.data[top.fieldName] = value;
            top.fieldName = undefined;
        } else {
            top.data.push(value);
        }
    }

    while (i < n) {
        const c = str[i];
        switch (c) {
            case '{': {
                stack.push(createNewObjectEntry());
                break;
            }
            case '[': {
                stack.push(createNewArrayEntry());
                break;
            }
            case '}':
            case ']': {
                const { data } = stack.pop();
                useValue(data);
                break;
            }
            case ',':
            case ':':
                break;
            default: {
                let accRawValue = '';
                let isString = false;
                if (c === '"') {
                    isString = true;
                    i++;
                }
                while (i < n && (isString ? str[i] !== '"' : ![',', ']', '}'].includes(str[i]))) {
                    accRawValue += str[i];
                    i++;
                }
                function processAccRawValue() {
                    if (isString) {
                        return accRawValue;
                    }
                    if ('0' <= c && c <= '9' || c === '-') {
                        return parseFloat(accRawValue);
                    }
                    if (accRawValue === 'true') {
                        return true;
                    }
                    if (accRawValue === 'false') {
                        return false;
                    }
                    if (accRawValue === 'null') {
                        return null;
                    }
                    throw new Error(1);
                }
                const value = processAccRawValue();
                const top = stack.length ? stack[stack.length - 1] : null;
                if (top?.type === STACK_ENTRY_TYPE.OBJECT && top.fieldName === undefined) {
                    top.fieldName = value;
                } else {
                    useValue(value);
                }
                if (str[i] === '"') {
                    i++;
                }
                continue;
            }
        }
        i++;
    }
    return result;
};