import functools
import heapq


def merge(*iterables, key=None):
    """
    Merge multiple sorted iterables into a single sorted iterable.
    Requires each sequence in iterables be already sorted with key, or by value if key not present.
    :param iterables: Iterable objects to merge
    :param key: optional, callable
                Key function, identical to that used by builtin sorted().
                If not present, items will be compared by value.
    :return: iterator to the sorted sequence
    """
    if key is None:
        for x in heapq.merge(*iterables):
            yield x
    else:
        bound_key = functools.partial(_add_key, key)
        with_key = map(bound_key, iterables)
        merged = heapq.merge(*with_key)
        for key, value in merged:
            yield value


def _add_key(key, iterable):
    for x in iterable:
        yield key(x), x