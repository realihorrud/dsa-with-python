class DoubleHashData:
    def __init__(self):
        self.table = [None] * 10

    def hash_function(self, key, i=0):
        return (self.primary_hash_function(key) + i * self.secondary_hash_function(key)) % 10

    # primary hash function
    def primary_hash_function(self, key):
        return (key) % 10

    # secondary hash function
    def secondary_hash_function(self, key):
        return 1 + key % 9

    # insert data to hash table
    def put(self, key):
        i = 0
        hash_value = self.hash_function(key)
        while self.table[hash_value]:
            # handle collision by probing using secondary hash functio
            i += 1
            hash_value = self.hash_function(key, i)  # use double hash
        # insert into the empty slot
        self.table[hash_value] = key

    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")

    # retrieve data from hash table
    def retrieve(self, key):
        hash_value = self.hash_function(key)
        i = 0
        while self.table[hash_value]:
            # if the required key is found, return its hash value and key
            if self.table[hash_value] == key:
                return {"hash_value": hash_value, "key": key}
            # move to the next slot using secondary hash function
            i += 1
            hash_value = self.hash_function(key, i)  # use double hash
        # if the key is not found in the table, return None
        return {"hash_value": hash_value, "key": None}


# keys
keys = [12, 17, 15, 4, 27, 14, 37]

hash1 = DoubleHashData()

# apply hash function to each key
for key in keys:
    hash1.put(key)

hash1.display()

print()
print("Retrieving Values: ")

print(hash1.retrieve(27))
print(hash1.retrieve(13))
