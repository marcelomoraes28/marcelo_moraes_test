from ..string_goal import which_size


class StringGoalTest:
    def test_which_size_greater_than(self):
        assert which_size('1.4', '1.2') == '1.4 is greater than 1.2'
        assert which_size('2', '1') == '2 is greater than 1'
        assert which_size('abc', 'ab') == 'abc is greater than ab'
        assert which_size('abc23', 'abc3') == 'abc23 is greater than abc3'

    def test_which_size_less_than(self):
        assert which_size('1.2', '1.4') == '1.2 is less than 1.4'
        assert which_size('1', '2') == '1 is less than 2'
        assert which_size('ab', 'abc') == 'ab is less than abc'
        assert which_size('abc3', 'abc34') == 'abc3 is less than abc34'

    def test_which_size_equal(self):
        assert which_size('1.2', '1.2') == '1.2 is equal to 1.2'
        assert which_size('2', '2') == '2 is equal to 2'
        assert which_size('abc', 'abc') == 'abc is equal to abc'
        assert which_size('abc34', 'abc34') == 'abc34 is equal to abc34'
