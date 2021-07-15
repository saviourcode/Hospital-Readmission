FROM python:3.6
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
COPY flask_poc.py /app
CMD ["python", "flask_poc.py"]~
