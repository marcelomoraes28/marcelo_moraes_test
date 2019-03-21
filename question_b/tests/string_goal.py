import pytest

from question_b.string_lib import StringLib


class TestStringGoal:
    def test_which_size_greater_than_with_the_same_types(self):
        assert StringLib.which_size('1.4', '1.2') == '1.4 is greater than 1.2'
        assert StringLib.which_size('abc23', 'abc3') == 'abc23 is greater than abc3'  # noqa
        assert StringLib.which_size('2', '1') == '2 is greater than 1'
        assert StringLib.which_size('abc', 'ab') == 'abc is greater than ab'

    def test_which_size_less_than_with_the_same_types(self):
        assert StringLib.which_size('1.2', '1.4') == '1.2 is less than 1.4'
        assert StringLib.which_size('1', '2') == '1 is less than 2'
        assert StringLib.which_size('ab', 'abc') == 'ab is less than abc'
        assert StringLib.which_size('abc3', 'abc34') == 'abc3 is less than abc34'  # noqa

    def test_which_size_equal_with_the_same_types(self):
        assert StringLib.which_size('1.2', '1.2') == '1.2 is equal to 1.2'
        assert StringLib.which_size('2', '2') == '2 is equal to 2'
        assert StringLib.which_size('abc', 'abc') == 'abc is equal to abc'
        assert StringLib.which_size('abc34', 'abc34') == 'abc34 is equal to abc34'  # noqa

    def test_which_size_greater_than_with_different_types(self):
        assert StringLib.which_size('1.4a', '1.2') == '1.4a is greater than 1.2'  # noqa
        assert StringLib.which_size('223', '1a') == '223 is greater than 1a'
        assert StringLib.which_size('411.22', 'ab') == '411.22 is greater than ab'  # noqa
        assert StringLib.which_size('4abc', '4') == '4abc is greater than 4'
        assert StringLib.which_size('4142.22', '4142') == '4142.22 is greater than 4142'  # noqa
        assert StringLib.which_size('123', '22.2') == '123 is greater than 22.2'  # noqa

    def test_which_size_less_than_with_different_types(self):
        assert StringLib.which_size('1.2', '1.4a') == '1.2 is less than 1.4a'
        assert StringLib.which_size('1a', '223') == '1a is less than 223'
        assert StringLib.which_size('ab', '411.22') == 'ab is less than 411.22'
        assert StringLib.which_size('4', '4abc') == '4 is less than 4abc'
        assert StringLib.which_size('4142', '4142.22') == '4142 is less than 4142.22'  # noqa
        assert StringLib.which_size('22.2', '123') == '22.2 is less than 123'

    def test_which_size_equal_with_different_types(self):
        assert StringLib.which_size('2.2c', '2222') == '2.2c is equal to 2222'
        assert StringLib.which_size('1.2', 'abc') == '1.2 is equal to abc'
        assert StringLib.which_size('abc2', '4444') == 'abc2 is equal to 4444'

    def test_which_size_invalid_input(self):
        with pytest.raises(ValueError):
            StringLib.which_size(1, 2)
        with pytest.raises(ValueError):
            StringLib.which_size(1.4, 2)
        with pytest.raises(ValueError):
            StringLib.which_size(1.4, '22')
        with pytest.raises(ValueError):
            StringLib.which_size([1], {"a": "b"})
        with pytest.raises(ValueError):
            StringLib.which_size((2.2,), (4, 4))
