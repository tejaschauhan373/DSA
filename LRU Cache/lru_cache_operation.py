from LRUCache import LRUCache

if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.put("mango", 10)
    lru_cache.put("apple", 20)
    lru_cache.put("guava", 30)
    print(lru_cache.most_recent_key())

    lru_cache.put("mango", 40)
    print(lru_cache.most_recent_key())

    order = lru_cache.get("mango")
    if order:
        print("Order of Mango is", order)

    lru_cache.put("banana", 20)

    print(lru_cache.cache)
    if lru_cache.get("apple") is None:
        print("Apple doesn't exist")

    if lru_cache.get("guava") is None:
        print("Guava doesn't exist")

    if lru_cache.get("banana") is None:
        print("Banana doesn't exist")

    if lru_cache.get("mango") is None:
        print("Mango doesn't exist")
