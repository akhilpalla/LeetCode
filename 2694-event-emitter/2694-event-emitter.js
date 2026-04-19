class EventEmitter {
    constructor() {
        this.events = new Map(); 
        this.subscriptions = []; 
    }

    subscribe(eventName, callback) {
        if (!this.events.has(eventName)) {
            this.events.set(eventName, []);
        }

        const callbacks = this.events.get(eventName);
        callbacks.push(callback);
        const index = this.subscriptions.length;
        this.subscriptions.push({ eventName, callback });

        return {
            unsubscribe: () => {
                const sub = this.subscriptions[index];
                if (!sub) return;
                const arr = this.events.get(sub.eventName);
                if (arr) {
                    const i = arr.indexOf(sub.callback);
                    if (i !== -1) arr.splice(i, 1);
                }
                this.subscriptions[index] = null;
            }
        };
    }

    emit(eventName, args = []) {
        const callbacks = this.events.get(eventName) || [];
        const results = [];
        for (const cb of callbacks) {
            results.push(cb(...args));
        }
        return results;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */