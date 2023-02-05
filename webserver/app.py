from flask import Flask, render_template, request
from redis import Redis
from rq import Queue

redis_conn = Redis.from_url('YOUR CONFIG HERE')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/send_job", methods=['POST'])
def send_job():
    input = request.get_json()
    print('input', input)
    q = Queue('t2i', connection=redis_conn)
    q.enqueue('sd_jobs.generate_image', 3, 4)

    return 'Job sent'

