FROM python:3.10.0-alpine
COPY . /app
RUN python3.10 -m pip install flask
WORKDIR /app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]