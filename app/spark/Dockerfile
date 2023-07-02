# Base image
FROM bitnami/spark:3.4.1

# Set up environment variables for Py4J
ENV PYTHONPATH="${SPARK_HOME}/python:${SPARK_HOME}/python/lib/py4j-0.10.9.7-src.zip:${PYTHONPATH}"