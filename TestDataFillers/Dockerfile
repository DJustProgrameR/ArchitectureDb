FROM python:3.9-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && apk add bash;
RUN pip3 install psycopg2-binary

CMD python -u src/filler.py
CMD python -u src/requests.py