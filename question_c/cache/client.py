import uuid

from multiprocessing import Process
from tenacity import retry, wait_fixed, stop_after_attempt

from .backend import MemcachedBackend, RedisBackend
from .exceptions import CacheClientException


class Client(object):
    ALLOWED_BACKENDS = [MemcachedBackend, RedisBackend]
    ALLOWED_TYPES = [dict, list, str, int, float, tuple]

    def __init__(self, backend, replicas=[]):
        self._backend = None
        self._replicas = []
        self.backend = backend
        self.replicas = replicas

    @property
    def backend(self):
        return self._backend

    def _validate_backed(self, backend):
        for allow_backend in self.ALLOWED_BACKENDS:
            if isinstance(backend, allow_backend):
                return
        raise CacheClientException("The backend only supports redis or memcache")  # noqa

    @backend.setter
    def backend(self, backend):
        self._validate_backed(backend)
        self._backend = backend

    @property
    def replicas(self):
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        if replicas:
            for replica in replicas:
                self._validate_backed(replica)
                self._replicas.append(replica)

    @retry(wait=wait_fixed(8), stop=stop_after_attempt(10))
    def set(self, data, **kwargs):
        """
        Set a new value in backend
        :return: key
        """
        if type(data) in self.ALLOWED_TYPES:
            key = str(uuid.uuid4())
            self.backend.set(key=key, value=data, **kwargs)
            if self.replicas:
                self.update_replicas(key=key, method='set', value=data, **kwargs)  # noqa
            return key
        raise CacheClientException("data must be" + " or ".join(self.ALLOWED_TYPES)) # noqa

    def delete(self, key, **kwargs):
        self.backend.delete(key, **kwargs)
        if self.replicas and 'is_replica' not in kwargs:
            self.update_replicas(key=key, method='delete', **kwargs)

    def update_replicas(self, method, **kwargs):
        """
        This method has the responsibility for updating all backend replicas
        :param method: 'delete' or 'set'
        :param kwargs:
        """
        for k, replica in enumerate(self.replicas):
            vars()['proc_' + str(k)] = Process(
                target=getattr(replica, method), kwargs=kwargs
            )
            vars()['proc_' + str(k)].start()

    def get(self, key):
        return self.backend.get(key)
