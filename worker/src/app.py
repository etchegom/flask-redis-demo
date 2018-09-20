import sys
from argparse import ArgumentParser
from redis import StrictRedis
import settings


def main(queue_name):
    try:
        redis = StrictRedis(host=settings.REDIS_HOST)
    except Exception:
        print("Failed to connect")
        sys.exit(1)

    while True:
        print("waiting for message in queue \"{}\" ...".format(queue_name))
        _, msg = redis.blpop(queue_name)
        print("recieved message {}".format(msg))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--queue-name', help='Queue name')
    args = parser.parse_args()
    main(queue_name=args.queue_name)
