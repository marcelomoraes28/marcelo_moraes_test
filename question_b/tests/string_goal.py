from ..string_goal import StringLib


class TestStringGoal:
    def test_which_size_greater_than_with_the_same_types(self):
        assert StringLib.which_size('1.4', '1.2') == '1.4 is greater than 1.2'
        assert StringLib.which_size('2', '1') == '2 is greater than 1'
        assert StringLib.which_size('abc', 'ab') == 'abc is greater than ab'
        assert StringLib.which_size('abc23', 'abc3') == 'abc23 is greater than abc3'

    def test_which_size_less_than_with_the_same_types(self):
        assert StringLib.which_size('1.2', '1.4') == '1.2 is less than 1.4'
        assert StringLib.which_size('1', '2') == '1 is less than 2'
        assert StringLib.which_size('ab', 'abc') == 'ab is less than abc'
        assert StringLib.which_size('abc3', 'abc34') == 'abc3 is less than abc34'

    def test_which_size_equal_with_the_same_types(self):
        assert StringLib.which_size('1.2', '1.2') == '1.2 is equal to 1.2'
        assert StringLib.which_size('2', '2') == '2 is equal to 2'
        assert StringLib.which_size('abc', 'abc') == 'abc is equal to abc'
        assert StringLib.which_size('abc34', 'abc34') == 'abc34 is equal to abc34'

    def test_which_size_greater_than_with_different_types(self):
        assert StringLib.which_size('1.4a', '1.2') == '1.4a is greater than 1.2'
        assert StringLib.which_size('223', '1a') == '223 is greater than 1a'
        assert StringLib.which_size('411.22', 'ab') == '411.22 is greater than ab'
        assert StringLib.which_size('4abc', '4') == '4abc is greater than 4'

    def test_which_size_less_than_with_different_types(self):
        assert StringLib.which_size('1.2', '1.4a') == '1.2 is less than 1.4a'
        assert StringLib.which_size('1a', '223') == '1a is less than 223'
        assert StringLib.which_size('411.22', 'ab') == 'ab is less than abc'
        assert StringLib.which_size('4', '4abc') == 'abc3 is less than abc34'

    def test_which_size_equal_with_different_types(self):
        assert StringLib.which_size('1.2', 'abc') == '1.2 is equal to 1.2'
        assert StringLib.which_size('22.2', '222') == '2 is equal to 2'
        assert StringLib.which_size('abc2', '4444') == 'abc is equal to abc'

