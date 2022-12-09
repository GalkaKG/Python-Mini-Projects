class CustomList:
    def __init__(self, *args):
        self.__data = list(args)

    def append(self, value):
        self.__data.append(value)
        return self.__to_result()

    def remove(self, index):
        el = self.get(index)
        self.__data.pop(index)
        return el

    def get(self, index):
        if index < 0 or index >= len(self.__data):
            raise Exception("Invalid index!")
        return self.__data[index]

    def extend(self, iterable):
        if len(iterable) == 0:
            raise Exception("Empty iterable")
        self.__data.extend(iterable)
        return self.__to_result()

    def insert(self, index, value):
        if index < 0 or index > len(self.__data):
            raise Exception("Invalid index")
        self.__data.insert(index, value)
        return self.__to_result()

    def pop(self):
        if not len(self.__data):
            raise Exception("The custom list is empty")
        return self.__data.pop()

    def clear(self):
        self.__data = []

    def index(self, value):
        for idx, el in enumerate(self.__data):
            if el == value:
                return idx
        return -1

    def reverse(self):
        return list(reversed(self.__data))

    def copy(self):
        return list(self.__data)

    def count(self, value):
        count = 0
        for el in self.__data:
            if el == value:
                count += 1

        return count

    def size(self):
        return len(self.__data)

    def add_first(self, value):
        return self.insert(0, value)

    def dictionize(self):
        result = {}
        for idx in range(0, len(self.__data), 2):
            key = self.__data[idx]
            value = self.__data[idx + 1] if idx + 1 < len(self.__data) else ' '
            result[key] = value
        return result

    def move(self, amount):
        self.__data = self.__data[amount:] + self.__data[:amount]
        return self.__to_result()

    def sum(self):
        result = 0
        for el in self.__data:
            if isinstance(el, int):
                result += el
            else:
                result += len(el)
        return result

    def overbound(self):
        max_value = float('-inf')
        max_idx = -1
        for idx, el in enumerate(self.__data):
            size = el if isinstance(el, int) else len(el)
            if size > max_value:
                max_value, max_idx = size, idx
        return max_idx

    def underbound(self):
        min_value = float('inf')
        min_idx = -1
        for idx, el in enumerate(self.__data):
            size = el if isinstance(el, int) else len(el)
            if size < min_value:
                min_value, min_idx = size, idx
        return min_idx

    def __to_result(self):
        return tuple(self.__data)
