from nose.tools import assert_equal, assert_raises


class TestSort(object):

    def test__sort(self):
        _sort = Sort()

        print('None input')
        assert_raises(TypeError, _sort.sort, None)

        print('Empty input')
        assert_equal(_sort.sort([]), [])

        print('One element')
        assert_equal(_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(_sort.sort(data), sorted(data))

        print('Success: test__sort\n')


def main():
    test = TestSort()
    test.test__sort()


if __name__ == '__main__':
    main()