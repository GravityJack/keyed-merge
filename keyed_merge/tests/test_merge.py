from keyed_merge import merge


def test_one_empty_sequence_gives_other_sequence():
    empty = []
    nonempty = list(range(5))
    result = merge(empty, nonempty)
    assert list(result) == nonempty


def test_same_length_sequences_default_key():
    evens = [0, 2, 4, 6]
    odds = [1, 3, 5, 7]
    result = merge(evens, odds)
    assert list(result) == list(range(8))


def test_different_length_sequences_default_key():
    evens = [0, 2, 4, 6]
    odds = [1, 3, 5]
    result = merge(odds, evens)
    assert list(result) == list(range(7))


def test_many_sequences_default_key():
    sequences = ([1, 2, 3],
                 (2, 4, 6),
                 [],
                 [5, 5, 9])
    result = merge(*sequences)
    assert list(result) == [1, 2, 2, 3, 4, 5, 5, 6, 9]


def test_comparable_objects():
    first = ['aa', 'bb']
    second = ['ab', 'ba']
    result = merge(first, second)
    assert list(result) == ['aa', 'ab', 'ba', 'bb']


def test_identity_key():
    def identity(x):
        return x
    evens = [0, 2, 4, 6]
    odds = [1, 3, 5, 7]
    result = merge(evens, odds, key=identity)
    assert list(result) == list(range(8))


def test_objects_and_attribute_key():
    class Dummy(object):
        def __init__(self, x):
            self.x = x
            self.key = -x

    objects = [Dummy(x) for x in range(4)]
    # reversed() maintains sort order by key field
    evens = reversed(objects[::2])
    odds = reversed(objects[1::2])
    result = merge(evens, odds, key=lambda o: o.key)
    correct = reversed(objects)
    assert list(result) == list(correct)


