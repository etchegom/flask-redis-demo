import uuid

from flask import Flask, request, jsonify
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config.from_object('settings')
redis_store = FlaskRedis(app)


@app.route('/demo', methods=['POST'])
def demo():
    assert 'data' in request.json
    assert 'queue_name' in request.json
    data = request.json.get('data')
    queue_name = request.json.get('queue_name')

    task_id = str(uuid.uuid4())

    redis_store.rpush(queue_name, {
        'task_id': task_id,
        'task_data': data
    })

    _, msg = redis_store.blpop(task_id)
    return jsonify(data=msg.get('task_result'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
