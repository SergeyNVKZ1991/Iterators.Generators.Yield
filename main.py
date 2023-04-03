# Exercise #1
class FlatIterator:
    def __init__(self, main_list):
        self.main_list = main_list
        self.lens = len(self.main_list)
        self.cursor = -1

    def __iter__(self):
        self.cursor += 1
        self.cursor_next = 0
        return self

    def __next__(self):
        if self.cursor_next == len(self.main_list[self.cursor]):
            iter(self)
        if self.cursor == self.lens:
            raise StopIteration
        self.cursor_next += 1
        return self.main_list[self.cursor][self.cursor_next - 1]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

# Exercise #2
import types
from collections.abc import Iterable


def flat_generator(list_of_lists, ignore_types=(str, bytes)):
    for x in list_of_lists:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from x
        else:
            yield

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_1()
    test_2()
