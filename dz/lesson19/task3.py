class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._data = list(range(start, end))

    def __iter__(self):
        return MyRangeIterator(self._data)

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")

        if index < 0 or index >= len(self._data):
            raise IndexError("Индекс вне диапазона")

        return self._data[index]

    def __len__(self):
        return len(self._data)


class MyRangeIterator:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration

        value = self._data[self._index]
        self._index += 1
        return value
