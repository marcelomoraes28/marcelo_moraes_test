import time
from .conftest import redis_client, redis_client_replicas, redis_backend_1, \
    redis_backend_2, memcache_client, memcache_backend_1, memcache_backend_2, \
    memcache_client_replicas, redis_client_with_memcache_replicas


class TestClientWithRedisAsBackend:
    def test_client_set_with_expiration_time_and_without_replicas(self):
        set_data = redis_client.set(data={"foo": "bar"}, expiration_time=2)
        assert redis_client.get(set_data) == {"foo": "bar"}
        time.sleep(3)
        assert redis_client.get(set_data) is None

    def test_client_set_without_replicas(self):
        set_data = redis_client.set({"foo": "bar"})
        assert set_data

    def test_client_get_without_replicas(self):
        set_data = redis_client.set({"foo": "bar"})
        assert set_data
        get_data = redis_client.get(set_data)
        assert get_data == {"foo": "bar"}

    def test_client_delete_without_replicas(self):
        set_data = redis_client.set({"foo": "bar"})
        assert set_data
        get_data = redis_client.get(set_data)
        assert get_data == {"foo": "bar"}
        redis_client.delete(set_data)
        assert redis_client.get(set_data) is None

    def test_client_get_with_replicas(self):
        set_data = redis_client_replicas.set({"foo": "bar"})
        assert set_data
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert redis_backend_1.get(set_data) == {"foo": "bar"}
        assert redis_backend_2.get(set_data) == {"foo": "bar"}

    def test_client_set_with_replicas(self):
        set_data = redis_client_replicas.set({"foo": "bar"})
        assert set_data
        get_data = redis_client_replicas.get(set_data)
        assert get_data == {"foo": "bar"}
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert get_data == redis_backend_1.get(set_data)
        assert get_data == redis_backend_2.get(set_data)

    def test_client_set_with_expiration_time_and_replicas(self):
        set_data = redis_client_replicas.set(data={"foo": "bar"}, expiration_time=4)  # noqa
        get_data = redis_client.get(set_data)
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert get_data == redis_backend_1.get(set_data)
        assert get_data == redis_backend_2.get(set_data)
        time.sleep(3)
        assert redis_backend_1.get(set_data) is None
        assert redis_backend_2.get(set_data) is None
        assert redis_client.get(set_data) is None

    def test_client_delete_with_replicas(self):
        set_data = redis_client_replicas.set({"foo": "bar"})
        assert set_data
        get_data = redis_client_replicas.get(set_data)
        assert get_data == {"foo": "bar"}
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert get_data == redis_backend_1.get(set_data)
        assert get_data == redis_backend_2.get(set_data)
        redis_client_replicas.delete(set_data)
        # This is a trick to give time to delete the data in the replicas =)
        time.sleep(1)
        assert redis_backend_1.get(set_data) is None
        assert redis_backend_2.get(set_data) is None
        assert redis_client_replicas.get(set_data) is None


class TestClientWithMemcachedAsBackend:
    def test_client_set_with_expiration_time_and_without_replicas(self):
        set_data = memcache_client.set(data={"foo": "bar"}, expiration_time=2)
        time.sleep(3)
        assert memcache_client.get(set_data) is None

    def test_client_set_without_replicas(self):
        set_data = memcache_client.set({"foo": "bar"})
        assert set_data

    def test_client_get_without_replicas(self):
        set_data = memcache_client.set({"foo": "bar"})
        assert set_data
        get_data = memcache_client.get(set_data)
        assert get_data == {"foo": "bar"}

    def test_client_delete_without_replicas(self):
        set_data = memcache_client.set({"foo": "bar"})
        assert set_data
        get_data = memcache_client.get(set_data)
        assert get_data == {"foo": "bar"}
        memcache_client.delete(set_data)
        assert memcache_client.get(set_data) is None

    def test_client_get_with_replicas(self):
        set_data = memcache_client_replicas.set({"foo": "bar"})
        assert set_data
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert memcache_backend_1.get(set_data) == {"foo": "bar"}
        assert memcache_backend_2.get(set_data) == {"foo": "bar"}

    def test_client_set_with_replicas(self):
        set_data = memcache_client_replicas.set({"foo": "bar"})
        assert set_data
        get_data = memcache_client_replicas.get(set_data)
        assert get_data == {"foo": "bar"}
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert get_data == memcache_backend_1.get(set_data)
        assert get_data == memcache_backend_2.get(set_data)

    def test_client_set_with_expiration_time_and_replicas(self):
        set_data = memcache_client_replicas.set(data={"foo": "bar"}, expiration_time=4)  # noqa
        get_data = memcache_client_replicas.get(set_data)
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert get_data == memcache_backend_1.get(set_data)
        assert get_data == memcache_backend_2.get(set_data)
        time.sleep(3)
        assert memcache_backend_1.get(set_data) is None
        assert memcache_backend_2.get(set_data) is None
        assert memcache_client_replicas.get(set_data) is None

    def test_client_delete_with_replicas(self):
        set_data = memcache_client_replicas.set({"foo": "bar"})
        assert set_data
        get_data = memcache_client_replicas.get(set_data)
        assert get_data == {"foo": "bar"}
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert get_data == memcache_backend_1.get(set_data)
        assert get_data == memcache_backend_2.get(set_data)
        memcache_client_replicas.delete(set_data)
        # This is a trick to give time to delete the data in the replicas =)
        time.sleep(1)
        assert memcache_backend_1.get(set_data) is None
        assert memcache_backend_2.get(set_data) is None
        assert memcache_client_replicas.get(set_data) is None


class TestClientMixinBackend:
    def test_client_get_with_replicas(self):
        set_data = redis_client_with_memcache_replicas.set({"foo": "bar"})
        assert set_data
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert memcache_backend_1.get(set_data) == {"foo": "bar"}
        assert memcache_backend_2.get(set_data) == {"foo": "bar"}

    def test_client_set_with_replicas(self):
        set_data = redis_client_with_memcache_replicas.set({"foo": "bar"})
        assert set_data
        get_data = redis_client_with_memcache_replicas.get(set_data)
        assert get_data == {"foo": "bar"}
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert get_data == memcache_backend_1.get(set_data)
        assert get_data == memcache_backend_2.get(set_data)

    def test_client_delete_with_replicas(self):
        set_data = redis_client_with_memcache_replicas.set({"foo": "bar"})
        assert set_data
        get_data = redis_client_with_memcache_replicas.get(set_data)
        assert get_data == {"foo": "bar"}
        # This is a trick to give time to record data in the replicas =)
        time.sleep(1)
        assert get_data == memcache_backend_1.get(set_data)
        assert get_data == memcache_backend_2.get(set_data)
        redis_client_with_memcache_replicas.delete(set_data)
        # This is a trick to give time to delete the data in the replicas =)
        time.sleep(1)
        assert memcache_backend_1.get(set_data) is None
        assert memcache_backend_2.get(set_data) is None
        assert redis_client_with_memcache_replicas.get(set_data) is None
