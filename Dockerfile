FROM python:3.13

RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /usr/local/app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]














