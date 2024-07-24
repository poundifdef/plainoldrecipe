ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

