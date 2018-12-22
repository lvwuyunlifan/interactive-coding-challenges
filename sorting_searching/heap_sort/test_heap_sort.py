from nose.tools import assert_equal, assert_raises


class TestHeapSort(object):

    def test_heap_sort(self):
        heap_sort = HeapSort()

        print('None input')
        assert_raises(TypeError, heap_sort.sort, None)

        print('Empty input')
        assert_equal(heap_sort.sort([]), [])

        print('One element')
        assert_equal(heap_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        
        assert_equal(heap_sort.sort(data), sorted(data))
        print('Success hibbard: test_heap_sort\n')


def main():
    
    test = TestHeapSort()
    test.test_heap_sort()


if __name__ == '__main__':
    main()