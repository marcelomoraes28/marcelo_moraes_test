import pytest

from ..cache.backend import RedisBackend, MemcachedBackend
from ..cache.exceptions import CacheException


class TestBackends:
    def test_invalid_port(self):
        with pytest.raises(CacheException):
            RedisBackend(host='localhost', port='foo-bar')
        with pytest.raises(CacheException):
            MemcachedBackend(host='localhost', port='foo-bar')