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

    # Return the index of the item we're searching for within our array, return -1 if not found
    def find(self, item):
        for i in range(self._size):
            if self._array[i] is item:          # Check if current value of array is strictly equal to the given item
                return i                        # Found the item, return its index
        return -1                               # Didn't find the item, return -1

    # (Private) Resize the array with the given (new) capacity
    def _resize(self, new_capacity):
        _temp_array = Array(new_capacity)  # Allocate desired memory to a temporary array
        for i in range(self._size):
            _temp_array[i] = self._array[i]  # Copy each value from the original array to the temporary array
        self._array = _temp_array  # Update the original array to its resized version
        _temp_array = None  # Deallocate memory from temporary array
        self._capacity = new_capacity  # Update the capacity so it matches the resized array
