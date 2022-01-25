FROM python:3.9.10

WORKDIR /usr/app/backend

COPY requirements.txt requirements.txt
RUN apt-get update && \
      apt-get -y install sudo
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=flask_app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python", "flask_app.py"]

EXPOSE 3000