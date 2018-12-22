from nose.tools import assert_equal, assert_raises


class TestCountSort(object):

    def test_count_sort(self):
        count_sort = CountSort()
        
        print('None input')
        assert_raises(TypeError, count_sort.sort, None)

        print('Empty input')
        assert_equal(count_sort.sort([]), [])

        print('One element')
        assert_equal(count_sort.sort([5]), [5])

        print('Two or more elements， have negative')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(count_sort.sort(data), sorted(data))
        print('Success negative data: test_count_sort\n')
        
        print('Two or more elements')

        data1 = [5, 1, 7, 2, 6, 3, 5, 7, 10]
        assert_equal(count_sort.sort(data1), sorted(data1))
        print('Success: test_count_sort\n')
        
def main():

    
    test = TestCountSort()
    test.test_count_sort()


if __name__ == '__main__':
    main()