FROM python:3.9

COPY ./app/CreateTopic.py .

RUN pip install confluent-kafka

CMD ["python", "CreateTopic.py"]
