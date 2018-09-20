FROM python:3.6.4-stretch

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

RUN mkdir -p /code
WORKDIR /code
ADD ./src /code

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
