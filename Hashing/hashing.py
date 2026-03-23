class HashData:
    def __init__(self):
        self.size = 5
        self.table = [None] * self.size
        self.lf_treashold = 0.75

    def hash_function(self, key):
        return key % self.size

    def put(self, item):
        hash_value = self.hash_function(item)
        self.table[hash_value] = item

        current_lf = sum(1 for slot in self.table if slot) / self.size
        if current_lf >= self.lf_treashold:
            self.rehash()

    def rehash(self):
        self.size *= 2
        new_table = [None] * self.size
        for data in self.table:
            if (data):
                hash_value = self.hash_function(data)
                new_table[hash_value] = data
        self.table = new_table
    
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")    

hash1 = HashData()
keys = list(map(int, input().split()))

for key in keys:
    hash1.put(key)

hash1.display()