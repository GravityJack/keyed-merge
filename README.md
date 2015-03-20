# keyed-merge
A Python 3 merge function which accepts a key argument.


## Why? Heapq doesn't cut it
The `heapq` module provides a `merge` function, but it 

## Installation
To install, clone this repo and copy the `keyed_merge` directory into your project.

## Usage
`merge` can function as a drop-in replacement for `heapq.merge`:

```python
>>> from keyed_merge import merge
>>> merged_lists = merge([1,3,5], [2, 4])
>>> list(merged_lists)
[1, 2, 3, 4, 5]
```

The real benefit is that it can accept a `key` argument, just like the built-in `sorted()` does. Suppose we have a class `Widget` that isn't comparable:

```python
>>> class Widget(object):
...     def __init__(self, x):
...         self.x = x
...
>>> even_widgets = [Widget(x) for x in range(0, 5, 2)]
>>> odd_widgets = [Widget(x) for x in range(1, 5, 2)]
```

`heapq.merge` doesn't support non-comparable objects:
```python
>>> import heapq
>>> merged_widgets = heapq.merge(even_widgets, odd_widgets)  # so far, so good
>>> list(merged_widgets)  # bummer
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/Cellar/python3/3.4.3/Frameworks/Python.framework/Versions/3.4/lib/python3.4/heapq.py", line 371, in merge
    heapify(h)
TypeError: unorderable types: Widget() < Widget()
```

Fortunately, you can provide a key to compare these objects to `merge`:
```python
>>> merged_widgets = merge(even_widgets, odd_widgets, key=lambda w: w.x)
>>> for widget in merged_widgets:
...     print(widget.x)
...
0
1
2
3
4
```

If `key` is provided, note that the iterables provided to `merge` must be sorted in ascending order by `key`.