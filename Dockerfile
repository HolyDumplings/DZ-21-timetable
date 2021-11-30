FROM python:3.8-slim
ENV PYTHONUNBUFFERED True
WORKDIR /DZ-21-timetable
COPY *.txt .
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt
COPY . ./

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:DZ-21-timetable
