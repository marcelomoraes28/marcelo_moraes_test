
CacheLib
=======================================

What is CacheLib?
----------------------------------
This library was basead on my current cache library [Scrooge](https://github.com/marcelomoraes28/scrooge_cache).

CacheLib is a python library for storing cached values ​​in the master backend, and if you want, you can replicate the data to multiple replicas.


How can I use?
-------------

**Rules:**
- If you do not set expiration_time cache_lib will take infinite time;
- If you use redis backend you can defined the db index using the parameter db=index, if you do not do this the default will be 0;
- It's not necessary set replicas if you don't want;

Installing
-------------
```
pip install -i https://test.pypi.org/simple/ cache-lib
```
Quick start
-----------
**Example using redis as backend**

```python
from cache import RedisBackend, Client

# Using Redis as backend
backend = RedisBackend(host='localhost', port=6379)
client = Client(backend=backend)

# Setting data
set_data = client.set({"foo": "bar"})
# Return the key Eg: 638e22f6-1957-4a59-a758-9d51853fa34f

# Retrieving data
get_data = client.get(set_data)
# Retrieve {"foo": "bar"}

# Delete data
client.delete(set_data)

```

**Example using memcached as backend**

```python
from cache import MemcachedBackend, Client

# Using Memecached as backend
backend = MemcachedBackend(host='localhost', port=6379)
client = Client(backend=backend)

# Setting data
set_data = client.set({"foo": "bar"})
# Return the key Eg: 638e22f6-1957-4a59-a758-9d51853fa34f

# Retrieving data
get_data = client.get(set_data)
# Retrieve {"foo": "bar"}

# Delete data
client.delete(set_data)

```

**Example with expiration time**

```python
from cache import MemcachedBackend, Client
import time

# Using Memecached as backend
backend = MemcachedBackend(host='localhost', port=6379)
client = Client(backend=backend)

# Setting data with expiration time in 50 seconds
set_data = client.set(data={"foo": "bar"}, expiration_time=50)
# Return the key Eg: 638e22f6-1957-4a59-a758-9d51853fa34f

time.sleep(51)

# Retrieving data
get_data = client.get(set_data)
# Retrieve None

```

**Example with replication data**
```python
from cache import MemcachedBackend, RedisBackend, Client

# Using Redis as the default backend and another Redis and Memcache as replicas
backend = RedisBackend(host='localhost', port=6379)
replica_1 = MemcachedBackend(host='localhost', port=11211)
replica_2 = RedisBackend(host='localhost2', port=6379)
client = Client(backend=backend, replicas=[replica_1, replica_2])

# Setting data
set_data = client.set({"foo": "bar"})
# Return the key Eg: 638e22f6-1957-4a59-a758-9d51853fa34f

# Retrieving data
get_data = client.get(set_data)
# Retrieve {"foo": "bar"}

# Delete data
client.delete(set_data)

```

Run tests
------------
**Important:** Make sure that docker and docker-compose already installed on your PC.

In the question_c dir you should run:
```
docker-compose up --abort-on-container-exit
```
