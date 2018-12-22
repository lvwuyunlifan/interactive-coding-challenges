from nose.tools import assert_equal, assert_raises


class TestBucketSort(object):

    def test_bucket_sort(self):
        bucket_sort = BucketSort()
        
        print('None input')
        assert_raises(TypeError, bucket_sort.sort, None)

        print('Empty input')
        assert_equal(bucket_sort.sort([]), [])

        print('One element')
        assert_equal(bucket_sort.sort([5]), [5])

        print('Two or more elements， have negative')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(bucket_sort.sort(data), sorted(data))
        print('Success negative data: test_bucket_sort\n')
        
        print('Two or more elements')
        data1 = [5, 1, 7, 2, 6, 3, 5, 7, 10]
        assert_equal(bucket_sort.sort(data1), sorted(data1))
        print('Success: test_bucket_sort\n')


def main():
    test = TestBucketSort()
    test.test_bucket_sort()


if __name__ == '__main__':
    main()