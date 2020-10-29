FROM python:latest

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
ENTRYPOINT ["flask"]

# dev server should not use in product mode(we can uwsgi for exemple) !!
CMD ["run", "--host", "0.0.0.0"] 
