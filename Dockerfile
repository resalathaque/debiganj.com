FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y libpq-dev python3-dev gettext

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app/

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "app.wsgi:application"]