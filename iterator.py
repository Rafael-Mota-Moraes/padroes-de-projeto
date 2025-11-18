from collections.abc import Iterable, Iterator


class MyIterator(Iterator):
    def __init__(self, collection) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self):
        self._items = []

    def add(self, value):
        self._items.append(value)

    def __iter__(self):
        return MyIterator(self._items)

    def __str__(self):
        return f'{self.__class__.__name__}({self._items})'


# iterator = MyIterator()
iterable = MyList()
iterable.add('Rafael')
iterable.add('Maria')
iterable.add('João')

print(iterable)

for value in iterable:
    print(value)
