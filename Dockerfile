FROM python:3.13
WORKDIR /usr/local/app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python3", "manage.py", "migrate"]

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]














