import json
import sys
from argparse import ArgumentParser
from redis import StrictRedis
import settings


def main(queue_name):
    try:
        redis = StrictRedis(host=settings.REDIS_HOST,
                            charset="utf-8", decode_responses=True)
    except Exception:
        print("Failed to connect")
        sys.exit(1)

    while True:
        print("waiting for message in queue \"{}\" ...".format(queue_name))
        _, msg = redis.blpop(queue_name)
        print("received message {}".format(msg))
        print(type(msg))

        content = json.loads(msg)
        task_id = content.get('task_id')
        task_data = content.get('task_data')

        print("send task result to {}".format(task_id))
        redis.rpush(task_id, {
            'task_result': task_data
        })


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--queue-name', help='Queue name')
    args = parser.parse_args()
    main(queue_name=args.queue_name)
