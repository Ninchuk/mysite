FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /mysite
COPY requirements.txt /mysite/
RUN pip install -r requirements.txt
COPY . /mysite/
RUN chmod +x /mysite/scripts/django/run_service.sh