from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config.from_object('settings')
redis_store = FlaskRedis(app)


@app.route('/')
def hello_world():
    # redis_store.rpush()
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
