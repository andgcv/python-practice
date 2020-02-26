from my_array import Array

if __name__ == '__main__':
    capacity = 4
    array = Array(capacity)

    # Tests with initial values and capacity of 4
    print('Array size: {}'.format(array.get_size()))                             # Should return 0
    print('Array capacity: {}'.format(array.get_capacity()))                     # Should return 4
    print('Array is empty: {}'.format(array.is_empty()))                         # Should return True
    print('')

    # Push items into the array
    array.push(7)
    array.push(30)
    print('Array value at index 0: {}'.format(array.at(0)))                      # Should return 7
    print('Find index of item 30: {}'.format(array.find(30)))                    # Should return 1
    print('')

    # Reach max capacity and resize the array
    array.push(3)
    array.push(10)
    array.push(2)
    print('Array size after pushing values: {}'.format(array.get_size()))        # Should return 5
    print('Capacity after resizing Array: {}'.format(array.get_capacity()))      # Should return 8
    print('Array is empty, after pushing values: {}'.format(array.is_empty()))   # Should return False
    print('Array value at index 4, after resizing: {}'.format(array.at(4)))      # Should return 2
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
