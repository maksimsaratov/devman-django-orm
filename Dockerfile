FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /devman
COPY devman/ /devman/
RUN pip install -r requirements.txt
