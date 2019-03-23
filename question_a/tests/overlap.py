import pytest

from question_a.overlap import Overlap


class TestOverlap:
    def test_invalid_type_of_payload(self):
        with pytest.raises(ValueError):
            Overlap.overlap('foo', 'bar')
        with pytest.raises(ValueError):
            Overlap.overlap(('foo', 'bar'), (1, 5))

    def test_overlap_is_true(self):
        assert Overlap.overlap((1, 5), (2, 6))
        assert Overlap.overlap((1, 10), (9, 14))
        assert Overlap.overlap((3, 9), (4, 10))
        assert Overlap.overlap((6, 15), (7, 16))

    def test_overlap_is_false(self):
        assert Overlap.overlap((1, 5), (6, 8)) is False
        assert Overlap.overlap((5, 11), (12, 13)) is False


