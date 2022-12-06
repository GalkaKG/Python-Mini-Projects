class HashTable:
    """
     Upon initialization the default length of the array should be 4.
     After each addition of an element if the HashTable gets too populated,
     double the length of the array and re-add the existing data
    """

    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity

    def get(self, key, default=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default

    def add(self, key, value):
        self[key] = value

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if self.__max_capacity == self.get_size():
            self.__resize()

        index = self.__calc_index(key)
        index = self.__get_free_index(index)

        self.__keys[index] = key
        self.__values[index] = value

    def __len__(self):
        return self.get_size()

    def __calc_index(self, key):  # get random index
        if type(key) == int:
            return key % self.__max_capacity
        return sum([ord(char) for char in key]) % self.__max_capacity

    def __get_free_index(self, index):
        if index == self.__max_capacity:
            index = 0

        if self.__keys[index] is None:
            return index

        return self.__get_free_index(index + 1)

    def get_size(self):
        return len([el for el in self.__keys if el is not None])

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__max_capacity
        self.__values = self.__values + [None] * self.__max_capacity
        self.__max_capacity *= 2

    def __str__(self):
        key_value_pairs = []
        for i in range(self.__max_capacity):
            if self.__keys[i] is not None:
                key_value_pairs.append(f"{self.__keys[i]}: {self.__values[i]}")

        return "{" + ", ".join(key_value_pairs) + "}"


# Test Code
table = HashTable()

table["name"] = "Peter"
table["age"] = 25
table["is_pet_owner"] = False
table["is_driver"] = True
table["new_name"] = "Ivan"

table["name"] = "Galina"
table.add(5, "5")

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
