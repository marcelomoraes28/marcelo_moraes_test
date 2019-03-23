from ..cache.backend import RedisBackend, MemcachedBackend
from ..cache.client import Client

redis_backend_default = RedisBackend(host='redis_default', port=6379)
redis_backend_1 = RedisBackend(host='redis_1', port=6379)
redis_backend_2 = RedisBackend(host='redis_2', port=6379)
memcache_backend_default = MemcachedBackend(host='memcache_default', port=11211)
memcache_backend_1 = MemcachedBackend(host='memcache_1', port=11211)
memcache_backend_2 = MemcachedBackend(host='memcache_2', port=11211)

redis_client = Client(backend=redis_backend_default)
memcache_client = Client(backend=memcache_backend_default)

redis_client_replicas = Client(backend=redis_backend_default,
                               replicas=[redis_backend_1, redis_backend_2])
memcache_client_replicas = Client(backend=memcache_backend_default,
                                  replicas=[memcache_backend_1,
                                            memcache_backend_2])

redis_client_with_memcache_replicas = Client(backend=redis_backend_default,
                                             replicas=[memcache_backend_1,
                                                       memcache_backend_2])
