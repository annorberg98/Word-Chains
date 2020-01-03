# Minimal iterable container. Example use:
#     bag = None              # create empty bag
#     bag = add(item, bag)    # add item to bag
#     for item in bag:        # iterate over nonempty bag
#     for item in bag or []:  # iterate over bag that might be empy (i.e. None)
#
# Jesper Larsson, Malmö University, 2018

class _Link:
    def __init__(self, item, next):
        self._item = item; self._next = next

    def __iter__(self):
        return _Iterator(self)

class _Iterator:
    def __init__(self, list):
        self._list = list

    def __next__(self):
        l = self._list
        if l is None:
            raise StopIteration
        else:
            self._list = l._next
            return l._item

def add(item, bag):
    return _Link(item, bag)
