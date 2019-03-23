import logging
import pickle
import redis

from pymemcache.client import base as memcache
from .exceptions import CacheException


class BaseBackend(object):
    cache_backend = None

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._con = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if not str(port).isdigit():
            raise CacheException("Port must be numbers")
        self._port = port

    def get(self, key):
        try:
            logging.info(f'Tryin to retrieve key data {key}')
            return pickle.loads(self._con.get(key))
        except TypeError:
            logging.error(f'Error to retrieve key data {key}')
            return None

    def set(self, key, value, **kwargs):
        logging.info(f'Saving data {key}')
        self._con.set(key, pickle.dumps(value), **kwargs)

    def delete(self, key):
        logging.info(f'Delete key data {key}')
        return self._con.delete(key)


class RedisBackend(BaseBackend):
    cache_backend = redis

    def __init__(self, db=0, **kwargs):
        super().__init__(**kwargs)
        self._con = self.cache_backend.Redis(host=self.host, port=self.port,
                                             db=db)

    def set(self, **kwargs):
        """
        Overwrite set method to translate expiration_time to redis pattern
        """
        if kwargs.get('expiration_time'):
            expiration_time = kwargs['expiration_time']
            del kwargs['expiration_time']
            super().set(ex=expiration_time, **kwargs)
        else:
            super().set(**kwargs)


class MemcachedBackend(BaseBackend):
    cache_backend = memcache

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._con = self.cache_backend.Client((self.host, self.port))

    def set(self, **kwargs):
        """
        Overwrite set method to translate expiration_time to memcache pattern
        """

        if kwargs.get('expiration_time'):
            expiration_time = kwargs['expiration_time']
            del kwargs['expiration_time']
            super().set(expire=expiration_time, **kwargs)
        else:
            super().set(**kwargs)
