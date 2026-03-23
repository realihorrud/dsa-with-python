class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}:{self.value}"


class HashMap:
    def __init__(self):
        self.table_size = 128
        self.table = [[] for _ in range(self.table_size)]

    def _hash_function(self, key):
        return key % self.table_size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair.key == key:
                pair.value = value
                return
        self.table[index].append(KeyValuePair(key, value))

    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair.key == key:
                del self.table[index][i]
                return

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair.key == key:
                return pair.value

    def __str__(self):
        map_str = ""
        for i, bucket in enumerate(self.table):
            if bucket:  # Only print non-empty buckets
                map_str += f"Bucket {i}: {', '.join(str(pair) for pair in bucket)}\n"
        return map_str


# Create a hashmap instance
student_map = HashMap()

# Insert values into map
student_map.insert(1, "James")
student_map.insert(2, "Paul")
student_map.insert(129, "Jake")

print("Hashmap Contents Before Deletion")
print(student_map)

# Remove student with ID 1
student_map.remove(1)

print("Hashmap Contents After Deletion")
print(student_map)
