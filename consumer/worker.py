#!/usr/bin/env python
from redis import Redis
from rq import Worker

# Preload libraries
# import library_that_you_want_preloaded

redis_conn = Redis.from_url('YOUR CONFIG HERE')

# Provide the worker with the list of queues (str) to listen to.
w = Worker(['t2i'], connection=redis_conn)
w.work()
