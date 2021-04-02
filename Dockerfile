FROM python:3

ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

ADD job /job


ENV PYTHONPATH=/job

WORKDIR /

ENTRYPOINT python -m job
