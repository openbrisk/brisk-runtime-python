FROM python:3.5-alpine

RUN apk update && \
    apk add --no-cache python3 python3-dev build-base && \
    pip3 install --upgrade pip && \
    rm -r /root/.cache

WORKDIR /app
COPY ./src .

RUN pip3 install -r requirements.txt && pip3 install flask

# Use flask?
ENTRYPOINT ["python3"]
CMD ["server.py"]