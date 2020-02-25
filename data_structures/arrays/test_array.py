from my_array import Array

if __name__ == '__main__':
    array = Array(4)

    print('Array size: {}'.format(array.get_size()))            # Should return 0
    print('Array capacity: {}'.format(array.get_capacity()))    # Should return 4
    print('Array is empty: {}'.format(array.is_empty()))        # Should return True
    print('Array value at index 0: {}'.format(array.at(0)))     # Should raise an Exception
