from redis import Redis
from rq import Queue

redis_conn = Redis.from_url('YOUR CONFIG HERE')
q = Queue('t2i', connection=redis_conn)
q.enqueue('sd_jobs.generate_image', 3, 4)