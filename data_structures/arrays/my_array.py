# Array (mutable, resizable)
class Array:

    # Declare the necessary values used for the Array
    _capacity = None
    _size = None
    _array = None

    # Initialize these values with the capacity chosen
    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity

    # Return the current size of the Array (how many items are in it)
    def get_size(self):
        return self._size

    # Return the current capacity of the Array (how many items it can hold)
    def get_capacity(self):
        return self._capacity

    # Return whether the Array is empty (True) or not (False)
    def is_empty(self):
        return True if self._size == 0 else False

    # Return the item at a given index, if the index is within bounds
    def at(self, index):
        if index < 0 or index >= self._size:         # Check if the index is within bounds, if not, raise Exception
            raise IndexError('Must enter a valid index')
        return self._array[index]

