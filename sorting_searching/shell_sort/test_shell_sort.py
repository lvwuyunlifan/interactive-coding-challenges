from nose.tools import assert_equal, assert_raises


class TestShellSort(object):

    def test_shell_sort(self):
        shell_sort = ShellSort()

        print('None input')
        assert_raises(TypeError, shell_sort.sort, None)

        print('Empty input')
        assert_equal(shell_sort.sort([]), [])

        print('One element')
        assert_equal(shell_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(shell_sort.sort(data, "hibbard"), sorted(data))
        print('Success hibbard: test_shell_sort\n')
        
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(shell_sort.sort(data, "ciura"), sorted(data))
        print('Success ciura: test_shell_sort\n')



def main():
    test = TestShellSort()
    test.test_shell_sort()


if __name__ == '__main__':
    main()