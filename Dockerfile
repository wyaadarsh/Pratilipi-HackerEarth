FROM python:3.7-slim
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PIP_INDEX_URL='https://pypi.python.org/simple'

RUN apt-get update

COPY requirements.txt /tmp/requirements.txt
RUN pip install -Ur /tmp/requirements.txt

RUN rm -rf /tmp/requirements*

COPY . /usr/src/app
ENV PORT 7070
EXPOSE 7070
ENTRYPOINT ["python"]
CMD ["app.py"]
