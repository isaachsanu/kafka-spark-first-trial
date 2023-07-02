FROM python:3.9

COPY ./app/consumer.py .

RUN pip install confluent-kafka

CMD ["python", "consumer.py"]