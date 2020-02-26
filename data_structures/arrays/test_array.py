from my_array import Array

if __name__ == '__main__':
    capacity = 4
    array = Array(capacity)

    print('-- Beginning of testing --')
    print('')

    # Tests with initial values and capacity of 4
    print('Array size: {}'.format(array.get_size()))                                        # Should return 0
    print('Array capacity: {}'.format(array.get_capacity()))                                # Should return 4
    print('Array is empty: {}'.format(array.is_empty()))                                    # Should return True
    print('')

    # Push items into the array
    array.push(7)
    array.push(30)
    print('Array value at index 0: {}'.format(array.at(0)))                                 # Should return 7
    print('Find index of item 30: {}'.format(array.find(30)))                               # Should return 1
    print('')

    # Reach max capacity and resize the array
    array.push(3)
    array.push(10)
    array.push(2)
    print('Array size after pushing values: {}'.format(array.get_size()))                   # Should return 5
    print('Capacity after resizing Array: {}'.format(array.get_capacity()))                 # Should return 8
    print('Array is empty, after pushing values: {}'.format(array.is_empty()))              # Should return False
    print('Array value at index 4, after resizing: {}'.format(array.at(4)))                 # Should return 2
    print('')

    # Insert items into the head, the middle, and the tail of the array
    array.insert(0, 15)
    print('Array value at index 0, after inserting at 0: {}'.format(array.at(0)))           # Should return 15
    array.insert(3, 4)
    print('Array value at index 3, after inserting at 3: {}'.format(array.at(3)))           # Should return 4
    array.insert(7, 9)
    print('Array value at index 7, after inserting at 7: {}'.format(array.at(7)))           # Should return 9
    print('Array value at index 1, after inserting all values: {}'.format(array.at(1)))     # Should return 7
    print('Array size after inserting all values: {}'.format(array.get_size()))             # Should return 8
    print('Capacity after inserting all values: {}'.format(array.get_capacity()))           # Should return 8
    print('')

    # Prepend items into the head of the array (will resize)
    array.prepend(1)
    print('Array value at index 0, after prepending value 1: {}'.format(array.at(0)))       # Should return 1
    array.prepend(42)
    print('Array value at index 0, after prepending value 42: {}'.format(array.at(0)))      # Should return 42
    print('Array size after prepending all values: {}'.format(array.get_size()))            # Should return 10
    print('Capacity after prepending all values: {}'.format(array.get_capacity()))          # Should return 16
    print('')

    # Pop items from the tail of the array
    print('Value of the item popped from the tail: {}'.format(array.pop()))                 # Should return 9
    print('Value of the item popped from the tail: {}'.format(array.pop()))                 # Should return 2
    print('Value of the item popped from the tail: {}'.format(array.pop()))                 # Should return 10
    print('')

    # Delete items from the array at the given indexes
    print('Value of the item deleted at first index: {}'.format(array.delete(0)))           # Should return 42
    print('Value of the item deleted at index 3: {}'.format(array.delete(3)))               # Should return 30
    print('Value of the item deleted at last index: {}'.format(array.delete(array.get_size()-1)))  # Should return 3
    print('')

    # Remote items from the array, with the given values
    print('Index of the item 15 removed: {}'.format(array.remove(15)))                      # Should return 1
    print('Index of the item 4 removed: {}'.format(array.remove(4)))                        # Should return 2
    print('Index of the item 7 removed: {}'.format(array.remove(7)))                        # Should return 1
    print('Index of the item 1 removed: {}'.format(array.remove(1)))                        # Should return 0
    # print('Index of the item 30 removed: {}'.format(array.remove(30)))                    # Should raise ValueError
    print('')

    # Size, capacity and if empty or not, after all tests
    print('Array size, after all the tests: {}'.format(array.get_size()))                   # Should return 0
    print('Array capacity, after all the tests: {}'.format(array.get_capacity()))           # Should return 1
    print('Array is empty, after all the tests: {}'.format(array.is_empty()))               # Should return True
    print('')

    print('-- End of testing --')
