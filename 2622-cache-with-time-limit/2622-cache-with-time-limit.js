class TimeLimitedCache {
    constructor() {
        this.cache = new Map();
    }
    
    set(key, value, duration) {
        const now = Date.now();
        const existed = this.cache.has(key) && now <= this.cache.get(key).expiredAt;
        this.cache.set(key, { value, expiredAt: now + duration });
        return existed;
    }
    
    get(key) {
        const entry = this.cache.get(key);
        const now = Date.now();
        return entry && now <= entry.expiredAt ? entry.value : -1;
    }
    
    count() {
        const now = Date.now();
        return Array.from(this.cache.values()).filter(entry => now <= entry.expiredAt).length;
    }
}


/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */