from LRUCache import LRUCache

if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.insert_key_value("mango", 10)
    lru_cache.insert_key_value("apple", 20)
    lru_cache.insert_key_value("guava", 30)
    print(lru_cache.most_recent_key())

    lru_cache.insert_key_value("mango", 40)
    print(lru_cache.most_recent_key())

    order = lru_cache.get_value("mango")
    if order:
        print("Order of Mango is", order)

    lru_cache.insert_key_value("banana", 20)

    if lru_cache.get_value("apple") is None:
        print("Apple doesn't exist")

    if lru_cache.get_value("guava") is None:
        print("Guava doesn't exist")

    if lru_cache.get_value("banana") is None:
        print("Banana doesn't exist")

    if lru_cache.get_value("mango") is None:
        print("Mango doesn't exist")
